// SPDX-License-Identifier: MIT
pragma solidity >=0.6.0 <0.9.0;

contract SimpleStorage {

    using SafeMath for uint256;

    bool public isLocked = false;
    bool public donationsAreLocked = false;
    bool public fundraiserCompleted = false;

    address public owner;

    string private upiID;
    string private bank_details_ifscCode;
    string private bank_details_bankName;
    string private bank_details_accountHolderName;
    string private bank_details_bankAccountNumber;

    uint256 public fundraiserTarget;
    uint256 public activeMilestone = 0;
    uint256 public withdrawableAmount = 0;
    uint256 public fundraiserAmountRaised = 0;
    uint256 public minimumDonationAmount = 100;
    uint256 public minimumWithdrawalAmount = 100;

    struct Milestone {
        bool achieved;
        bool votingActive;
        uint256 numberOfVotes;
        uint256 amountToBeReleased;
        string milestoneDescription;
        mapping(address => bool) votersPool;
    }

    // Milestones
    uint256 numberOfMilestones = 0;
    Milestone[] public fundraiserMilestones;

    // Donations
    uint256 numberOfDonations = 0;
    uint256 numberOfDonors = 0;
    mapping(address => uint256) public fundraiserDonations;

    constructor (
            string memory _bank_details_accountHolderName,
            string memory _bank_details_ifscCode,
            string memory _bank_details_bankName,
            string memory _bank_details_bankAccountNumber,
            string memory _upiID,
            uint256 _fundraiserTarget
        ) public {
        owner = msg.sender;

        upiID = _upiID;
        fundraiserTarget = _fundraiserTarget;
        bank_details_bankName = _bank_details_bankName;
        bank_details_ifscCode = _bank_details_ifscCode;
        bank_details_accountHolderName = _bank_details_accountHolderName;
        bank_details_bankAccountNumber = _bank_details_bankAccountNumber;
    }

    // ====================== modifiers ======================

    modifier onlyOwner {
        require(msg.sender == owner, "Fundzin: Caller is not the Contract Owner. Access Denied.");
        _;
    }

    modifier onlyIfFundraiserIsActive {
        require(fundraiserCompleted == false,"Fundzin : The Fundraiser has now been Completed");
        // emit FundraiserCompleted("Fundzin : The Fundraiser has now been Completed");
        _;
    }

    function getOwner() public view returns(address) {
        return owner;
    }

    // ====================== milestone logic ======================

    // list of event definitions
    event ContractLocked(string _message);
    event MilestoneCompleted(string _message);
    event FundraiserCompleted(string _message);
    event MaximumMilestoneLimitReached(string _message);
    event ContractLockedChangesRejected(string _message);
    event VoteRejected(address _voterAddress , string _message);
    event NewMilestoneAdded(string _milestoneDescription, uint256 _amountToBeReleased, string _message);
    event InvalidMilestoneEnquiry(uint256 _milestoneNumberEnquired, uint256 _totalMilestones, string _message);

    // adding a new milestone
    function addMilestone(
            string calldata _milestoneDescription,
            uint256 _amountToBeReleased
        ) external onlyOwner returns(bool) {

        if(numberOfMilestones >= 10) {
            emit MaximumMilestoneLimitReached("Fundzin : Max Milestone Limit Reached");
            return false;
        }

        if(isLocked == true) {
            emit ContractLockedChangesRejected("Fundzin : The Contract has been Locked . Request Rejected");
            return false;
        }

        Milestone memory newMilestone = Milestone({
            milestoneDescription : _milestoneDescription,
            amountToBeReleased : _amountToBeReleased,
            votingActive : false,
            achieved : false,
            numberOfVotes : 0
        });
        fundraiserMilestones.push(newMilestone);
        numberOfMilestones = numberOfMilestones.add(1);
        emit NewMilestoneAdded(_milestoneDescription, _amountToBeReleased, "Fundzin : New Milestone has been added");
    }

    // get the number of milestones
    function getNumberOfMilestones() public view returns(uint256) {
        return numberOfMilestones;
    }

    // get the milestone description
    // Note: 0 based indexing .
    function getMilestoneDescription(uint256 _milestoneNumber) public returns(string memory) {
        if(_milestoneNumber >= numberOfMilestones){
            emit InvalidMilestoneEnquiry(_milestoneNumber,numberOfMilestones,"Fundzin : Invalid Milestone Number");
        }
        return fundraiserMilestones[_milestoneNumber].milestoneDescription;
    }

    // get the milestone amount
    // Note: 0 based indexing
    function getMilestoneAmount(uint256 _milestoneNumber) public returns(uint256) {
        if(_milestoneNumber >= numberOfMilestones){
            emit InvalidMilestoneEnquiry(_milestoneNumber,numberOfMilestones,"Fundzin : Invalid Milestone Number");
        }
        return fundraiserMilestones[_milestoneNumber].amountToBeReleased;
    }

    // get the milestone voting state
    // Note: 0 based indexing
    function getMilestoneVotingState(uint256 _milestoneNumber) public returns(bool){
        if(_milestoneNumber >= numberOfMilestones){
            emit InvalidMilestoneEnquiry(_milestoneNumber,numberOfMilestones,"Fundzin : Invalid Milestone Number");
        }
        return fundraiserMilestones[_milestoneNumber].votingActive;
    }

    // get the milestone acheived status (whether the milestone has been achieved)
    // Note: 0 based indexing
    function getMilestoneAchievedStatus(uint256 _milestoneNumber) public returns(bool){
        if(_milestoneNumber >= numberOfMilestones){
            emit InvalidMilestoneEnquiry(_milestoneNumber,numberOfMilestones,"Fundzin : Invalid Milestone Number");
        }
        return fundraiserMilestones[_milestoneNumber].achieved;
    }

    // check the whether a vote has been cast from the given voter address
    // Note: 0 based indexing
    function checkVotedStatus(uint256 _milestoneNumber, address _voterAddress) public returns(bool){
        if(_milestoneNumber >= numberOfMilestones){
            emit InvalidMilestoneEnquiry(_milestoneNumber,numberOfMilestones,"Fundzin : Invalid Milestone Number");
        }
        if(!isDonor(_voterAddress)) emit VoteRejected(_voterAddress, "Fundzin : User is not a donor to the fundraiser. Vote Rejected");
        return fundraiserMilestones[_milestoneNumber].votersPool[_voterAddress];
    }

    // lock the contract
    function lockContract() external onlyOwner returns(bool) {
        if(isLocked == true) {
            emit ContractLockedChangesRejected("Fundzin : Contract is already locked");
            return false;
        }
        isLocked = true;
        emit ContractLocked("Fundzin : The contract has been Locked. Further changes will be rejected");
        return true;
    }

    // ====================== donation logic ======================

    // list of event definitions
    event DonationsLocked(address _donor , uint256 _amount , string _message);
    event DonationAmountTooLow(address _donor, uint256 _amount, string _message);

    // initiate a new donation
    function newDonation(address _donor, uint256 _amount) external returns(bool) {
        if(donationsAreLocked == false){
            if(_amount < minimumDonationAmount) {
                emit DonationAmountTooLow(_donor,_amount,"Fundzin : Donation amount below minimum Threshold");
                return false;
            }

            numberOfDonations = numberOfDonations.add(1);
            if(fundraiserDonations[_donor] == 0) numberOfDonors = numberOfDonors.add(1);
            fundraiserDonations[_donor] = fundraiserDonations[_donor].add(_amount);
            fundraiserAmountRaised = fundraiserAmountRaised.add(_amount);

            if(fundraiserAmountRaised > fundraiserTarget){
                donationsAreLocked = true;
            }

            return true;
        }
        else {
            emit DonationsLocked(_donor,_amount,"Fundzin : Fundraiser Target has been achieved . Donations have been locked !");
            return false;
        }
    }

    // get the number of donations made
    function getNumberOfDonations() public view returns(uint256) {
        return numberOfDonations;
    }

    // get the number of unique donors who donated
    function getNumberOfDonors() public view returns(uint256) {
        return numberOfDonors;
    }

    // get the total amount raised by the fundraiser
    function getFundraiserAmountRaised() public view returns(uint256) {
        return fundraiserAmountRaised;
    }

    // check whether a given address is a donor or not
    function isDonor(address _donorAddress) public view returns(bool) {
        if(fundraiserDonations[_donorAddress] > 0) return true; else return false;
    }

    // ====================== voting logic ======================

    // list of event definitions
    event VotingAlreadyActive(string _message);
    event VoteCasted(address _voterAddress, string _message);
    event VotingNotActive(address _voterAddress, string _message);
    event DoubleVotingRejected(address _voterAddress, string _message);

    // initiate voting for the current milestone
    function activateVotingForCurrentMilestone() external onlyOwner returns(bool){
        if(fundraiserMilestones[activeMilestone].votingActive == true){
            emit VotingAlreadyActive("The milestone is already accepting votes");
            return false;
        }
        else{
            fundraiserMilestones[activeMilestone].votingActive = true;
            return true;
        }
    }

    // cast vote if the current milestone is accepting votes and if the voter is a donor
    function castVote(address _voterAddress) public returns(bool) {
        if(!isDonor(_voterAddress)){
            emit VoteRejected(_voterAddress,"Fundzin : Voter is not a Donor. Vote Rejected");
            return false;
        }

        if(fundraiserMilestones[activeMilestone].votingActive == false){
            emit VotingNotActive(_voterAddress, "Fundzin : Voting is not yet active for the current milestone");
            return false;
        }

        else{
            if(fundraiserMilestones[activeMilestone].votersPool[_voterAddress] == true){
                emit DoubleVotingRejected(_voterAddress,"Fundzin : You have already voted");
                return false;
            }

            emit VoteCasted(_voterAddress,"Fundzin : Vote was casted successfully");
            fundraiserMilestones[activeMilestone].votersPool[_voterAddress] = true;
            fundraiserMilestones[activeMilestone].numberOfVotes = fundraiserMilestones[activeMilestone].numberOfVotes.add(1);

            if(fundraiserMilestones[activeMilestone].numberOfVotes > numberOfDonors / 2) {
                fundraiserMilestones[activeMilestone].achieved = true;
                fundraiserMilestones[activeMilestone].votingActive = false;

                if(fundraiserAmountRaised < (withdrawableAmount + fundraiserMilestones[activeMilestone].amountToBeReleased))
                    withdrawableAmount = fundraiserAmountRaised;
                else
                    withdrawableAmount = withdrawableAmount.add(fundraiserMilestones[activeMilestone].amountToBeReleased);

                activeMilestone = activeMilestone.add(1);
                emit MilestoneCompleted("Fundzin : Congratulations ! Current Milestone completed . Switched to next Milestone");

                if(activeMilestone == numberOfMilestones) {
                    fundraiserCompleted = true;
                    emit FundraiserCompleted("Fundzin : The Fundraiser has now been Completed");
                }
            }
            return true;
        }
    }

    // get the milestone number of the currently active milestone
    function currentMilestoneNumber() public view returns(uint256) {
        return activeMilestone;
    }

    // get the number of votes which have been cast for the currently active milestone
    function votesCastForCurrentMilestone() public onlyIfFundraiserIsActive view returns(uint256) {
        return fundraiserMilestones[activeMilestone].numberOfVotes;
    }

    // check if the fundraiser has been completed
    function isFundraiserCompleted() public view returns(bool) {
        return fundraiserCompleted;
    }

    // ====================== withdrawal logic ======================

    // list of event definitions
    event IllegalWithdrawalRequest(address _withdrawer, string _message);
    event InsufficientFunds(address _withdrawer, uint256 _amount, string _message);
    event GasFeeProtectionError(address _withdrawer, uint256 _amount, string _message);
    event WithdrawalAmountTooLow(address _withdrawer, uint256 _amount, string _message);

    // function for withdrawal of amount by the owner of the contract
    // thinking about adding a verification hash to the below command containing a hashed made up of
    // all the data such as bank details and owner address . Could be used for further verification
    function withdrawAmount(address _withdrawer, uint256 _amount) external onlyOwner returns(bool) {
        if(_withdrawer != owner) {
            emit IllegalWithdrawalRequest(_withdrawer,"Fundzin : The address attempted an unauthorized withdrawal");
            return false;
        }
        else{
            if(_amount > withdrawableAmount){
                emit InsufficientFunds(_withdrawer,_amount,"Fundzin : You dont have enough funds for this request to be granted");
                return false;
            }
            if(withdrawableAmount >= minimumWithdrawalAmount && _amount < minimumWithdrawalAmount) {
                emit WithdrawalAmountTooLow(_withdrawer,_amount,"Fundzin : Withdrawal amount too low");
                return false;
            }
            else{
                if((withdrawableAmount-_amount) < minimumWithdrawalAmount){
                    emit GasFeeProtectionError(_withdrawer,_amount,"Fundzin : GasFeeProtectionError ");
                }
            }
        }
    }
}

// library to make sure that we dont overflow our integers under any circumstance . 256 bits => 32 bytes
library SafeMath {
    // check for integer overflows during addition
    function add(uint256 a, uint256 b) internal pure returns (uint256) {
        uint256 c = a + b;
        // if c < a => integer has wrapped around itself . Hence , overflow .
        require(c >= a, "SafeMath : addition overflow");
        return c;
    }
    // check for negative balances during subtraction
    function sub(uint256 a, uint256 b) internal pure returns (uint256) {
        require(b<=a, "SafeMath: subtraction overflow");
        uint256 c = a - b;
        return c;
    }
}
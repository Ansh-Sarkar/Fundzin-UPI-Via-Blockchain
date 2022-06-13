//SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.6.0 <0.9.0;

contract Voting{

    // structure : vote
    struct vote {
        address voterAddress;
        bool choice;
    }

    // structure : voter
    struct voter {
        string voterName;
        // we dont know the option selected, we just want to whether the voter
        // address has casted a vote or not (boolean state : either true or false)
        bool voted;
    }

    // ====================== variables ======================

    // declaring the variables which we will be using in the contract
    uint private countResult = 0;
    uint public finalResult = 0;
    uint public totalVoter = 0;
    uint public totalVote = 0;

    // official address of this ballot
    address public ballotOfficialAddress;
    string public ballotOfficialName;
    string public proposal;

    // what we want to achieve based on this vote
    // mappings to maintain voters list
    mapping(uint => vote) private votes;
    mapping(address => voter) public voterRegister;

    // defining the state of the smart contract
    // created state, voting state, ended state
    enum State{Created, Voting , Ended}
    State public state;

    // ====================== modifiers ======================

    // checks a condition and works only if the condition returns true
    modifier condition(bool _condition){
        require(_condition, "An Internal Condition failed !");
        _;
    }

    // modifier to allow only the owner to make changes
    modifier onlyOfficial(){
        require(msg.sender == ballotOfficialAddress,"Caller was not the owner");
        _;
    }

    // used to control which functions are active (can be used) in which phase
    modifier inState(State _state){
        require(state == _state, "Current stage dosent match function state");
        _;
    }

    // ====================== functions ======================

    // constructor - initialize the smart contract
    constructor (
        string memory _ballotOfflicialName,
        string memory _proposal
    ) public {
        ballotOfficialAddress = msg.sender;
        ballotOfficialName = _ballotOfflicialName;
        proposal = _proposal;
        state = State.Created;
    }

    // add voter
    function addVoter(address _voterAddress, string memory _voterName) public inState(State.Created) onlyOfficial {
        voter memory v;
        v.voterName = _voterName;
        v.voted = false;
        voterRegister[_voterAddress] = v;
        totalVoter++;
    }

    // start the voting period
    function startVote() public inState(State.Created) onlyOfficial {
        state = State.Voting;
    }

    // cast vote
    function doVote(bool _choice) public inState(State.Voting) returns(bool voted) {
        bool found = false;
        if(bytes(voterRegister[msg.sender].voterName).length != 0 && !voterRegister[msg.sender].voted){
            voterRegister[msg.sender].voted = true;
            vote memory v;
            v.voterAddress = msg.sender;
            v.choice = _choice;
            if(_choice) {
                countResult++;
            }
            votes[totalVote] = v;
            totalVote++;
            found = true;
        }
        return found;
    }

    // end the voting period
    function endVote() public inState(State.Voting) onlyOfficial {
        state = State.Ended;
        finalResult = countResult;
    }

}

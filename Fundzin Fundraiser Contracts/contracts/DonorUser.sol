// SPDX-License-Identifier: MIT
pragma solidity >=0.6.0 <0.9.0;

contract DonorUser {

    using UserSafeMath for uint256;

    address public owner;

    string private email;
    string private hashed_password;

    uint256 private total_donations;

    bool public deleted;
    bool public kyc_completed;

    mapping(string => bool) donations;

    constructor(string memory _email, string memory _hashed_password) public {
        owner = msg.sender;
        email = _email;
        hashed_password = _hashed_password;
        total_donations = 0;
        kyc_completed = false;
        deleted = false;
    }

    modifier onlyOwner {
        require(msg.sender == owner, "Fundzin: Caller is not the Contract Owner. Access Denied.");
        _;
    }

    modifier ifNotDeleted {
        require(deleted == false, "The user you are trying to access has been deleted !");
        _;
    }

    // view owner functions . in our case , fundzin will always be the owner of every user \
    // smart contract
    function getOwner() public ifNotDeleted view returns(address) {
        return owner;
    }

    // password functions
    function getHashedPassword() public view onlyOwner returns(string memory) {
        return hashed_password;
    }

    // allowing the owner to update the password
    function updatePassword(string memory _newPassword) public onlyOwner returns(bool) {
        hashed_password = _newPassword;
        return true;
    }

    // donation functions
    function getTotalDonations() public view onlyOwner returns(uint256) {
        return total_donations;
    }

    function incrementDonations(uint256 number) public onlyOwner returns(bool){
        total_donations = total_donations.add(number);
        return true;
    }

    function decrementDonations(uint256 number) public onlyOwner returns(bool){
        total_donations = total_donations.sub(number);
        return true;
    }

    // email id functions
    function getEmailID() public view onlyOwner returns(string memory) {
        return email;
    }

    function updateEmailID(string memory _newEmail) public onlyOwner returns(bool) {
        email = _newEmail;
        return true;
    }

    // function for deleting the user
    function deleteUser() public onlyOwner returns(bool){
        deleted = true;
        return true;
    }

}

// library to make sure that we dont overflow our integers under any circumstance . 256 bits => 32 bytes
library UserSafeMath {
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
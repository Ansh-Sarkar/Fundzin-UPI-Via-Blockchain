// SPDX-License-Identifier: MIT
// pragma solidity >=0.6.0 <0.9.0;

// contract SimpleStorage {
//     using SafeMath for uint256;
//     struct Milestone {

//     }


//     this will be initialized to 0
//     uint256 favouriteNumber;

//     address public owner;

//     constructor(uint256 _favouriteNumber) public {
//         favouriteNumber = _favouriteNumber;
//         owner = msg.sender;
//     }

//     struct People{
//         uint256 favouriteNumber;
//         string name;
//     }

//     People[] public people;
//     mapping(string => uint256) public nameToFavouriteNumber;

//     function getOwner() public view returns(address) {
//         return owner;
//     }

//     function store(uint256 _favouriteNumber) public {
//         favouriteNumber = _favouriteNumber;
//     }

//     function retrieve() public view returns(uint256) {
//         return favouriteNumber;
//     }

//     function addPerson(string memory _name, uint256 _favouriteNumber) public {
//         people.push(People(_favouriteNumber,_name));
//         nameToFavouriteNumber[_name] = _favouriteNumber;
//     }
// }

// library to make sure that we dont overflow our integers under any circumstance . 256 bits => 32 bytes
// library SafeMath {
//     check for integer overflows during addition
//     function add(uint256 a, uint256 b) internal pure returns (uint256) {
//         uint256 c = a + b;
//         if c < a => integer has wrapped around itself . Hence , overflow .
//         require(c >= a, "SafeMath : addition overflow");
//         return c;
//     }
//     check for negative balances during subtraction
//     function sub(uint256 a, uint256 b) internal pure returns (uint256) {
//         require(b<=a, "SafeMath: subtraction overflow");
//         uint256 c = a - b;
//         return c;
//     }
// }

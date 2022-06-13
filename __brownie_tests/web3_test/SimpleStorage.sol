// SPDX-License-Identifier: MIT

pragma solidity ^0.6.0;

contract SimpleStorage {

    uint256 favouriteNumber;
    bool favouriteBool;

    // Structure: People
    struct People{
        uint256 favouriteNumber;
        string name;
    }

    // people
    People[] public people;
    mapping(string => uint256) public nameToFavouriteNumber;

    // ====================== functions ======================

    // store a number
    function store(uint256 _favouriteNumber) public {
        favouriteNumber = _favouriteNumber;
    }

    // retrieve the stored number
    function retrieve() public view returns(uint256) {
        return favouriteNumber;
    }

    // add a new person to the nameToFavouriteNumber mapping along with their favourite number
    function addPerson(string memory _name, uint256 _favouriteNumber) public {
        people.push(People(_favouriteNumber,_name));
        nameToFavouriteNumber[_name] = _favouriteNumber;
    }

}
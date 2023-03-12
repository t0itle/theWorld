Player Karma Smart Contract

pragma solidity ^0.6.0;

contract Character {
    // The character's karma score
    int public karma;

    // Relationship values with each of the 7 NPC gods
    mapping(string => int) public godRelationships;

    // Constructor function to initialize godRelationships to 0
    constructor() public {
        godRelationships["God 1"] = 0;
        godRelationships["God 2"] = 0;
        godRelationships["God 3"] = 0;
        godRelationships["God 4"] = 0;
        godRelationships["God 5"] = 0;
        godRelationships["God 6"] = 0;
        godRelationships["God 7"] = 0;
    }

    // Function to increase the character's karma
    function increaseKarma(int amount) public {
        karma += amount;
    }

    // Function to decrease the character's karma
    function decreaseKarma(int amount) public {
        karma -= amount;
    }

    // Function to increase or decrease the character's relationship with a god
    function changeGodRelationship(string memory godName, int amount) public {
        godRelationships[godName] += amount;
    }

    // Function to get the character's relationship value with a god
    function getGodRelationship(string memory godName) public view returns (int) {
        return godRelationships[godName];
    }

    // Function to get the character's overall relationship status with the 7 gods
    function getOverallGodRelationshipStatus() public view returns (string memory) {
        int overallRelationship = 0;

        for (uint i = 1; i <= 7; i++) {
            overallRelationship += godRelationships["God " + uint2str(i)];
        }

        if (overallRelationship >= 50) {
            return "Beloved by the gods";
        } else if (overallRelationship >= 25) {
            return "Favored by the gods";
        } else if (overallRelationship >= 10) {
            return "Blessed by the gods";
        } else if (overallRelationship >= -10) {
            return "Neutral towards the gods";
        } else if (overallRelationship >= -25) {
            return "Disfavored by the gods";
        } else if (overallRelationship >= -50) {
            return "Rejected by the gods";
        } else {
            return "Hated by the gods";
        }
    }

    // Function to get the character's overall karma status
    function getOverallKarmaStatus() public view returns (string memory) {
        if (karma >= 50) {
            return "Saint";
        } else if (karma >= 25) {
            return "Virtuous";
        } else if (karma >= 10) {
            return "Moral";
        } else if (karma >= -10) {
            return "Neutral";
        } else if (karma >= -25) {
            return "Immoral";
        } else if (karma >= -50) {
            return "Evil";
        } else {
            return "Villain";
        }
    }

    // Function to convert uint to string
    function uint2str(uint i) internal pure returns (string memory) {
        if (i == 0) {
            return "0";
        }
        uint j = i;
        uint length;
        while (j != 0) {
            length++;
            j /= 10;
        }
        bytes memory b
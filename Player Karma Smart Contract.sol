Player Karma Smart Contract

pragma solidity ^0.6.0;

contract Character {
    // Other variables and functions go here

    // The character's karma score
    int public karma;

    // Function to increase the character's karma
    function increaseKarma(int amount) public {
        karma += amount;
    }

    // Function to decrease the character's karma
    function decreaseKarma(int amount) public {
        karma -= amount;
    }
}

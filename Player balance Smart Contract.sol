Player balance Smart Contract
pragma solidity ^0.5.0;

contract MyContract {
    // Declare variables
    uint public balance;
    mapping(address => uint) public playerBalances;
    address public owner;
    string public name;

    // Constructor function
    constructor() public {
        owner = msg.sender;
        name = "My RPG";
    }

    // Function to check the balance of a player
    function checkBalance(address _player) public view returns (uint) {
        return playerBalances[_player];
    }

    // Function to transfer funds from one player to another
    function transfer(address _to, uint _amount) public {
        require(playerBalances[msg.sender] >= _amount, "Insufficient funds");
        playerBalances[msg.sender] -= _amount;
        playerBalances[_to] += _amount;
    }

    // Function to add funds to the contract balance
    function addFunds(uint _amount) public {
        require(msg.sender == owner, "Only the owner can add funds");
        balance += _amount;
    }
}
Character Quest Completion Contract

pragma solidity ^0.6.0;

import "https://example.com/path/to/Quest.sol";

contract Character {
    // Other variables and functions go here

    // Mapping of quest IDs to rewards for quests completed by the character
    mapping(uint => uint) public questsCompleted;

    // Function to mark a quest as complete
    function completeQuest(uint questId, uint reward) public {
        // Add the quest ID and reward to the questsCompleted mapping
        questsCompleted[questId] = reward;
    }
}

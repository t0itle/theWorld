Character Solidity Smart Contract

pragma solidity ^0.6.0;

contract UniqueCharacters {
    // Define the characteristics of a unique character
    struct Character {
        string name;
        uint strength;
        uint intelligence;
        uint dexterity;
        uint charisma;
        uint luck;
        string jobClass;
        string specialAttribute;
    }

    // Mapping of character IDs to unique characters
    mapping(uint => Character) public characters;

    // ID of the next character to be minted
    uint public nextCharacterId = 0;

    // Mint a new unique character
    function mintCharacter(string memory _name, uint _strength, uint _intelligence, uint _dexterity, uint _charisma, uint _luck, string memory _jobClass, string memory _specialAttribute) public {
        // Create a new character with the specified characteristics
        Character memory character = Character(_name, _strength, _intelligence, _dexterity, _charisma, _luck, _jobClass, _specialAttribute);

        // Assign the character a unique ID and add it to the mapping
        characters[nextCharacterId] = character;
        nextCharacterId++;
    }
}
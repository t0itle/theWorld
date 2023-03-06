Side Character Solidity

pragma solidity ^0.7.0;

contract SideCharacter {
    // Enum of possible character races
    enum Race { Human, Elf, Dwarf, Orc }

    // Enum of possible character classes
    enum Class { Warrior, Mage, Rogue }

    // Struct for storing character data
    struct Character {
        string name;
        Race race;
        Class class;
        uint strength;
        uint intelligence;
        uint charisma;
    }

    // Mapping from random character IDs to character data
    mapping(bytes32 => Character) public characters;

    // Function to generate a new side character for the player
    function generateCharacter() public {
        // Generate random ID for character
        bytes32 id = sha3(abi.encodePacked(now, msg.sender));

        // Generate random name
        string memory name = generateName();

        // Generate random race
        Race memory race = Race(randomNumber(4));

        // Generate random class
        Class memory class = Class(randomNumber(3));

        // Generate random stats
        uint strength = randomNumber(10) + 1;
        uint intelligence = randomNumber(10) + 1;
        uint charisma = randomNumber(10) + 1;

        // Save character data to mapping
        characters[id] = Character(name, race, class, strength, intelligence, charisma);
    }

    // Function to delete a side character
    function deleteCharacter(bytes32 id) public {
        delete characters[id];
    }

    // Function to generate a random number between 0 and max (inclusive)
    function randomNumber(uint max) private view returns (uint) {
        return uint(keccak256(abi.encodePacked(block.difficulty, now, msg.sender))) % (max + 1);
    }

    // Function to generate a random name
    function generateName() private view returns (string memory) {
        // Array of possible first syllables
        string[7] memory firstSyllables = [            "A", "Be", "De", "El", "Fa", "Jo", "Ki"        ];

        // Array of possible second syllables
        string[7] memory secondSyllables = [            "bar", "ched", "dell", "fel", "gor", "hal", "jen"        ];

        // Generate random first and second syllables
        uint index1 = randomNumber(6);
        uint index2 = randomNumber(6);

        // Concatenate syllables to form name
        string memory name = firstSyllables[index1] + secondSyllables[index2];
        return name;
    }
}

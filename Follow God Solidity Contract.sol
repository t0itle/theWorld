Follow God Solidity Contract

pragma solidity ^0.7.0;

contract Character {
    string public name;
    mapping(string => uint) public stats;
    address public god;
    string[] public abilities;

    constructor(string memory _name, mapping(string => uint) memory _stats) public {
        name = _name;
        stats = _stats;
    }

    function followGod(address _god) public {
        god = _god;
        applyGodBonuses();
    }

    function stopFollowingGod() public {
        god = address(0);
        applyGodBonuses();
    }

    function applyGodBonuses() private {
        delete abilities;
        God godContract = God(god);
        for (uint i = 0; i < godContract.bonusesLength(); i++) {
            GodBonus memory bonus = godContract.bonuses(i);
            abilities.push(bonus.ability);
            stats[bonus.stat] += bonus.value;
        }
    }
}

contract God {
    string public name;
    struct GodBonus {
        string ability;
        string stat;
        uint value;
    }
    GodBonus[] public bonuses;

    function bonusesLength() public view returns (uint) {
        return bonuses.length;
    }

    function bonuses(uint index) public view returns (GodBonus memory) {
        return bonuses[index];
    }
}

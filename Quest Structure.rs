Quest Structure

struct Quest {
    QuestType type;
    string description;
    uint reward;
    address god;
    bool completed;
}

struct Player {
    string public name;
    address public owner;
    Quest[] public quests;
    uint public karma;

    function giveQuest(string memory _description, uint _reward) public {
        quests.push(Quest(QuestType.PlayerGiven, _description, _reward, address(0), false));
    }

    function completeQuest(uint index) public {
        Quest storage quest = quests[index];
        require(!quest.completed, "Quest already completed");
        quest.completed = true;
        // Give reward and update karma
        if (quest.type == QuestType.Regular) {
            owner.transfer(quest.reward);
        } else if (quest.type == QuestType.PlayerGiven) {
            karma += quest.reward;
        } else if (quest.type == QuestType.Karma) {
            require(karma >= quest.reward, "Not enough karma");
            karma -= quest.reward;
            owner.transfer(quest.reward * 2);
        } else if (quest.type == QuestType.God) {
            God godContract = God(quest.god);
            godContract.completeQuest(owner);
        }
    }
}

contract God {
    mapping(address => bool) public questsCompleted;

    function completeQuest(address player) public {
        questsCompleted[player] = true;
        // Give reward to player
    }
}
Player playerContract = Player(playerAddress);
playerContract.giveQuest("Defeat the dragon", 1000, dragonGodAddress);

contract Player {
    string public name;
    address public owner;
    Quest[] public quests;
    uint public karma;

    function completeQuest(uint index) public {
        Quest storage quest = quests[index];
        require(!quest.completed, "Quest already completed");
        quest.completed = true;
        // Give reward and update karma
        if (quest.type == QuestType.Regular) {
            owner.transfer(quest.reward);
        } else if (quest.type == QuestType.PlayerGiven) {
            karma += quest.reward;
        } else if (quest.type == QuestType.Karma) {
            require(karma >= quest.reward, "Not enough karma");
            karma -= quest.reward;
            owner.transfer(quest.reward * 2);
        } else if (quest.type == QuestType.God) {
            God godContract = God(quest.god);
            godContract.completeQuest(owner);
        }
    }
}

contract God {
    mapping(address => bool) public questsCompleted;

    function issueQuest(string description, uint reward, address player) public {
        Quest memory quest = Quest(QuestType.God, description, reward, address(this), false);
        Player playerContract = Player(player);
        playerContract.quests.push(quest);
    }

    function completeQuest(address player) public {
        questsCompleted[player] = true;
        // Give reward to player
    }
}

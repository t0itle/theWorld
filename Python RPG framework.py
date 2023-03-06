Python RPG framework
class Player:
    def __init__(self, name, level, hp, attack, defense):
        self.name = name
        self.level = level
        self.hp = hp
        self.attack = attack
        self.defense = defense
    
    def attack(self, other):
        damage = self.attack - other.defense
        other.hp -= damage
        print(f"{self.name} attacks {other.name} for {damage} damage!")
    
    def __repr__(self):
        return f"Player(name='{self.name}', level={self.level}, hp={self.hp}, attack={self.attack}, defense={self.defense})"

class NPC:
    def __init__(self, name, level, hp, attack, defense, reward):
        self.name = name
        self.level = level
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.reward = reward
    
    def attack(self, other):
        damage = self.attack - other.defense
        other.hp -= damage
        print(f"{self.name} attacks {other.name} for {damage} damage!")
    
    def __repr__(self):
        return f"NPC(name='{self.name}', level={self.level}, hp={self.hp}, attack={self.attack}, defense={self.defense}, reward={self.reward})"

class Game:
    def __init__(self):
        self.player = Player("Bob", 1, 100, 10, 5)
        self.npcs = [
            NPC("Goblin", 1, 50, 5, 3, 10),
            NPC("Troll", 2, 75, 8, 4, 20),
            NPC("Dragon", 3, 100, 12, 6, 50),
        ]
        self.location = "Forest"
    
    def fight(self, npc):
        print(f"You encounter a level {npc.level} {npc.name} in the {self.location}!")
        while self.player.hp > 0 and npc.hp > 0:
            self
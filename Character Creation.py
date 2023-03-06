import random

class Character:
    def __init__(self, name, questions, race, job_class):
        self.name = name
        self.questions = questions
        self.race = race
        self.job_class = job_class
        self.stats = {"strength": 0, "intelligence": 0, "dexterity": 0, "charisma": 0, "luck": 0}
        self.gold = 0
        self.inventory = []
        self.potions = {"health": 0, "mana": 0}
        self.special_attribute = None

        # Generate base stats
        self.stats["strength"] += random.randint(1, 10)
        self.stats["intelligence"] += random.randint(1, 10)
        self.stats["dexterity"] += random.randint(1, 10)
        self.stats["charisma"] += random.randint(1, 10)
        self.stats["luck"] += random.randint(1, 10)
    def generate_stats(self):
        # Apply race bonuses to stats
        if self.race == "Human":
            self.stats["strength"] += 1
            self.stats["intelligence"] += 1
            self.stats["dexterity"] += 1
            self.stats["charisma"] += 1
        elif self.race == "Elf":
            self.stats["dexterity"] += 2
            self.stats["charisma"] += 2
        elif self.race == "Dwarf":
            self.stats["strength"] += 2
            self.stats["intelligence"] += 2
        elif self.race == "Orc":
            self.stats["strength"] += 3
        
        # Modify stats based on player's answers to questions
        for question, answer in self.questions.items():
            if question == "Are you a risk taker?":
                if answer == "Yes":
                    self.stats["strength"] += 2
                    self.stats["dexterity"] += 2
                elif answer == "No":
                    self.stats["intelligence"] += 2
                    self.stats["charisma"] += 2
            elif question == "Do you prefer to be alone or in a group?":
                if answer == "Alone":
                    self.stats["intelligence"] += 2
                elif answer == "In a group":
                    self.stats["charisma"] += 2
            elif question == "Do you think you are lucky?":
                if answer == "Yes":
                    self.stats["luck"] += 2
            elif question == "Do you consider yourself more logical or creative?":
                if answer == "Logical":
                    self.stats["intelligence"] += 2
                elif answer == "Creative":
                    self.stats["charisma"] += 2
            # Add more questions and stat modifications here
    
    if self.job_class == "Warrior":
            self.inventory.append(Item("Sword", 10, 15))
            self.inventory.append(Item("Shield", 5, 10))
            self.potions["health"] += 3
        elif self.job_class == "Mage":
            self.inventory.append(Item("Staff", 5, 10))
            self.potions["mana"] += 3
        elif self.job_class == "Thief":
            self.inventory.append(Item("Dagger", 5, 10))
            self.potions["health"] += 2
            self.potions["mana"] += 1
        elif self.job_class == "Paladin":
            self.inventory.append(Item("Mace", 10, 15))
            self.inventory.append(Item("Shield", 5, 10))
            self.potions["health"] += 3
            self.potions["mana"] += 3
        elif self.job_class == "Ranger":
            self.inventory.append(Item("Bow", 10, 15))
            self.inventory.append(Item("Arrows", 0, 0))
            self.potions["health"] += 2
            self.potions["mana"] += 1
        elif self.job_class == "Bard":
            self.inventory.append(Item("Lute", 5, 10))
            self.potions["mana"] += 2
            self.potions["health"] += 1
        elif self.job_class == "Cleric":
            self.inventory.append(Item("Mace", 10, 15))
            self.inventory.append(Item("Shield", 5, 10))
            self.potions["mana"] += 3
            self.potions["health"] += 3
        # Add more job classes and starting equipment here
    def __str__(self):
        # Return a string representation of the character
        return f"Name: {self.name}\nStats: {self.stats}\nGold: {self.gold}\nInventory: {self.inventory}"





NPC Reproduction

import random

class NPC:
    def __init__(self, name, age, gender, reproducible):
        self.name = name
        self.age = age
        self.gender = gender
        self.reproducible = reproducible
        self.reproduced = False
    
    def reproduce(self, partner):
        if self.reproducible and partner.reproducible:
            # Determine chance of reproduction based on ages of NPCs
            age_difference = abs(self.age - partner.age)
            reproduction_chance = max(0, 100 - age_difference)
            # Reproduce with a random chance based on age difference
            if random.randint(1, 100) <= reproduction_chance:
                self.reproduced = True
                partner.reproduced = True
                # Create new NPC with random name, age 0, and gender
                return NPC(
                    random.choice(["Alice", "Bob", "Charlie", "Dave", "Eve"]),
                    0,
                    random.choice(["male", "female"]),
                    True,
                    nurtured=False
                )
        return None
    
    def nurture(self, nurturer):
        self.age += 1
        self.nurtured = True

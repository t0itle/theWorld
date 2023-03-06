NPC Lifespan

import random

class NPC:
    def __init__(self, age=0, lifespan=100):
        self.age = age
        self.lifespan = lifespan
        self.reproductive = False

    def age_npc(self):
        self.age += 1
        if self.age >= self.lifespan:
            self.die()
    
    def reproduce(self):
        if not self.reproduced:
            self.reproduced = True
            return NPC()
        return None
    
    def die(self):
        del self

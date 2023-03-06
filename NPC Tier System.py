NPC Tier System

class NPC:
    def __init__(self, name, tier):
        self.name = name
        self.tier = tier
        self.skills = []
        self.memory = []
        self.age = 0
        self.is_dead = False
        self.is_in_party = False
        if tier == 1:
            self.intelligence = "Basic Learning"
            self.learning_rate = 0.05
        elif tier == 2:
            self.intelligence = "Limited Learning"
            self.learning_rate = 0.01
        elif tier == 3:
            self.intelligence = "Self-Aware"
            self.learning_rate = 0.1

    def learn_skill(self, skill):
        if self.tier == 3:
            self.skills.append(skill)
        elif self.tier == 1:
            self.skills.append(skill)
            self.memory.append(skill)
            if len(self.memory) > 10:
                self.memory.pop(0)
        elif self.tier == 2:
            self.memory.append(skill)
            if len(self.memory) > 10:
                self.memory.pop(0)
                self.skills.append(random.choice(self.memory))
                self.memory.pop(random.choice(self.memory))
                
    def npc_age(self):
        self.age += 1
        if self.age > 80:
            self.is_dead = True
    def join_party(self):
        if self.tier == 3 or self.tier == 1:
            self.is_in_party = True
        else:
            print("NPC is not eligible to join the party")
    def leave_party(self):
        self.is_in_party = False

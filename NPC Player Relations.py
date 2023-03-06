NPC Player Relations

class Player:
    def __init__(self, name):
        self.name = name
        self.relationship_level = 0
    
    def interact(self, npc):
        # Increase relationship level with NPC based on random chance
        relationship_chance = random.randint(1, 100)
        if relationship_chance <= 50:
            self.relationship_level += 1
            npc.relationship += 1
        # If relationship level is high enough, receive gift or other benefit
        if self.relationship_level >= 10:
            # Choose random gift or benefit
            gift_or_benefit = random.choice(["gift", "information", "follow"])
            if gift_or_benefit == "gift":
                print("Received gift from NPC!")
            elif gift_or_benefit == "information":
                print("Received information from NPC!")
            elif gift_or_benefit == "follow":
                print("NPC is following player!")
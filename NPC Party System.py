NPC Party System

class NPC:
    def __init__(self, name, home_location):
        self.name = name
        self.home_location = home_location
        self.location = home_location  # NPCs start at home
        self.relationship_level = 0
    
    def go_home(self):
        self.location = self.home_location

class Party:
    def __init__(self, leader):
        self.leader = leader
        self.members = []
        self.max_distance = 10  # Maximum distance NPCs can be from the leader to join the party
        self.min_relationship_level = 10  # Minimum relationship level required to join the party
    
    def add_member(self, npc):
        distance = self.calculate_distance(self.leader.location, npc.location)
        if distance <= self.max_distance and npc.relationship_level >= self.min_relationship_level:
            self.members.append(npc)
        else:
            print("NPC is not eligible to join the party")
    
    def calculate_distance(self, location1, location2):
        # Calculate distance between two locations
        return distance

player = Player()
npc1 = NPC("Bob", "Village")
npc2 = NPC("Sue", "Forest")
party = Party(player)
party.add_member(npc1)
party.add_member(npc2)

# When the player logs off
party.disband()

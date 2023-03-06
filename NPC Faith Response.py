NPC Faith Response

class Player:
    def __init__(self, name, faith):
        self.name = name
        self.faith = faith

    def enter_town(self, town):
        if self.faith == town.god:
            print("The NPCs of the town welcome you warmly.")
        elif self.faith == "":
            print("The NPCs of the town try to convert you to their faith.")
        else:
            print("The NPCs of the town are hostile towards you.")

NPC Player Gifting

class Item:
    def __init__(self, name: str, value: int):
        self.name = name
        self.value = value

class NPC:
    def __init__(self, name: str):
        self.name = name
        self.inventory = []
    
    def receive_gift(self, item: Item):
        self.inventory.append(item)
        print(f"{self.name} received a gift of {item.name} from the player.")

class Player:
    def __init__(self, name: str):
        self.name = name
        self.inventory = []
    
    def gift_item(self, npc_name: str, item: Item):
        # Find the NPC in the player's list of NPCs
        npc = None
        for n in self.npcs:
            if n.name == npc_name:
                npc = n
                break
        
        # Check if the NPC exists
        if npc is None:
            print(f"Error: NPC {npc_name} not found.")
            return
        
        # Check if the player has the item in their inventory
        if item not in self.inventory:
            print(f"Error: {self.name} does not have {item.name} in their inventory.")
            return
        
        # Give the item to the NPC
        self.inventory.remove(item)
        npc.receive_gift(item)

# Example usage
player = Player("Bob")
npc1 = NPC("Alice")
npc2 = NPC("Eve")
player.npcs = [npc1, npc2]
item1 = Item("Sword", 100)
item2 = Item("Shield", 50)
player.inventory = [item1, item2]
player.gift_item("Alice", item1)
player.gift_item("Eve", item2)

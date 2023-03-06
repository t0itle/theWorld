Territory Python 

class Territory:
    def __init__(self, name, resources):
        self.name = name
        self.resources = resources

class Resource:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

class God:
    def __init__(self, name, territories, resources):
        self.name = name
        self.territories = territories
        self.resources = resources

# Create some territories and resources
troy = Territory("Troy", [])
greece = Territory("Greece", [])
egypt = Territory("Egypt", [])
wood = Resource("Wood", 1000)
stone = Resource("Stone", 500)
gold = Resource("Gold", 250)

# Create some gods and assign them territories and resources
zeus = God("Zeus", [troy, greece], [wood, stone, gold])
poseidon = God("Poseidon", [egypt], [stone, gold])
hades = God("Hades", [], [gold])

# Add resources to the territories
troy.resources.extend([wood, stone])
greece.resources.append(gold)
egypt.resources.extend([stone, gold])

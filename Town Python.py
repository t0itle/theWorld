Town Python

class Town:
    def __init__(self, name, location, size, population):
        self.name = name
        self.location = location
        self.size = size
        self.population = population
        self.buildings = []
        self.npcs = []
        self.god = god

    def add_building(self, building):
        self.buildings.append(building)

    def add_npc(self, npc):
        self.npcs.append(npc)
    def change_god(self, new_god):
        self.god = new_god
class God:
    def __init__(self, name, towns):
        self.name = name
        self.towns = towns

    def trade_town(self, other_god, town):
        if town in self.towns:
            self.towns.remove(town)
            other_god.towns.append(town)

    def attack_town(self, other_god, town):
        if town in other_god.towns:
            if self.power > other_god.power:
                other_god.towns.remove(town)
                self.towns.append(town)
            else:
                self.towns.remove(random.choice(self.towns))
                other_god.towns.append(random.choice(other_god.towns))

#Follow God with Stats Python

class Character:
    def __init__(self, name, stats, god=None):
        self.name = name
        self.stats = stats
        self.god = god

    def follow_god(self, god):
        self.god = god

    def stop_following_god(self):
        self.god = None

class Character:
    def __init__(self, name, stats, god=None):
        self.name = name
        self.stats = stats
        self.god = god
        self.abilities = []
        self.apply_god_bonuses()

    def follow_god(self, god):
        self.god = god
        self.apply_god_bonuses()

    def stop_following_god(self):
        self.god = None
        self.apply_god_bonuses()

    def apply_god_bonuses(self):
        # Remove any existing god bonuses
        self.abilities = [ability for ability in self.abilities if not isinstance(ability, GodBonus)]
        # If the character is following a god, add the god's bonuses
        if self.god is not None:
            self.abilities += self.god.bonuses

class GodBonus:
    def __init__(self, stat, value):
        self.stat = stat
        self.value = value

class God:
    def __init__(self, name, bonuses):
        self.name = name
        self.bonuses = bonuses

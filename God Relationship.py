God Relationship Python

class God:
    def __init__(self, name, personality_traits):
        self.name = name
        self.personality_traits = personality_traits
        self.relationships = {}

    def determine_relationship(self, other_god):
        # Check if the two gods have interacted before
        if other_god.name in self.relationships:
            # Return the existing relationship
            return self.relationships[other_god.name]
        else:
            # Calculate the probability of the two gods being enemies, neutral, or allies based on their personality traits
            enemy_probability = self.get_enemy_probability(other_god)
            neutral_probability = self.get_neutral_probability(other_god)
            ally_probability = self.get_ally_probability(other_god)
            # Use a random number generator to determine the relationship based on the probabilities
            relationship = self.generate_relationship(enemy_probability, neutral_probability, ally_probability)
            # Save the relationship in the two gods' relationship dictionaries
            self.relationships[other_god.name] = relationship
            other_god.relationships[self.name] = relationship
            # Return the relationship
            return relationship

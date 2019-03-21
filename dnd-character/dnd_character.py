from random import sample
from math import floor


def modifier(stat):
    return floor((stat - 10) / 2)


class Character:
    Abilities = ['strength', 'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma']

    def __init__(self):
        for i in self.Abilities:
            setattr(self, i, self.ability())
        self.hitpoints = modifier(self.constitution) + 10

    def ability(self):
        return sum(sorted(sample(range(1, 6), 4))[1:])

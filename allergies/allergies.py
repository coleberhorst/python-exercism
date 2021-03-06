class Allergies(object):
    allergens = {
        'eggs' : 1,
        'peanuts' : 2,
        'shellfish' : 4,
        'strawberries' : 8,
        'tomatoes' : 16,
        'chocolate' : 32,
        'pollen' : 64,
        'cats' : 128
    }

    def __init__(self, score):
        self.score = score

    def is_allergic_to(self, item):
        return bool(self.score & self.allergens[item])

    @property
    def lst(self):
        return [food for food, i in self.allergens.items() if self.score & i]

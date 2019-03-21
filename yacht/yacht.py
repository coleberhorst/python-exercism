# Score categories
# Change the values as you see fit
YACHT = 50
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 30
BIG_STRAIGHT = 31
CHOICE = 9


def score(dice, category):
    dice.sort()
    if category == YACHT and dice.count(dice[0]) == 5:
        return YACHT
    elif category >= ONES and category <= SIXES:
        return dice.count(category) * category
    elif category == FULL_HOUSE:
        if dice.count(dice[0]) in (2, 3) and dice.count(dice[-1]) in (2, 3):
            return sum(dice)
    elif category == FOUR_OF_A_KIND:
        if dice.count(dice[0]) >= 4:
            return dice[0] * 4
        elif dice.count(dice[-1]) >= 4:
            return dice[-1] * 4
    elif category == LITTLE_STRAIGHT and dice == [1, 2, 3, 4, 5]:
        return LITTLE_STRAIGHT
    elif category == BIG_STRAIGHT and dice == [2, 3, 4, 5, 6]:
        return 30
    elif category == CHOICE:
        return sum(dice)
    return 0

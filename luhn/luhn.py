class Luhn(object):
    def __init__(self, card_num):
        self.card_num = "".join(i for i in card_num if i.isdigit())
        self.valid = (self.card_num == card_num.replace(" ", ""))

    def is_valid(self):
        sum = 0
        for i, number in enumerate(self.card_num[::-1]):
            n = int(number)
            if (i-1) % 2 == 0:
                n *= 2
            if n > 9:
                sum += n - 9
            else:
                sum += n
        print(sum)
        return sum % 10 == 0 and len(self.card_num) > 1 and self.valid

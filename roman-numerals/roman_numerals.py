from math import floor, log10


roman_numerals = ["I", "X", "C", "M"]
half_roman_numerals = ["V", "L", "D"]


def numeral(number):
    result = ""
    count = 0
    while number and count != 4:
        place = floor(log10(number))
        digit = floor(number / (10**place))
        if digit == 9:
            result += roman_numerals[place] + roman_numerals[place + 1]
        elif digit >= 5:
            result += half_roman_numerals[place] + roman_numerals[place] * (digit - 5)
        elif digit == 4:
            result += roman_numerals[place] + half_roman_numerals[place]
        else:
            result += roman_numerals[place] * digit
        number -= 10**place * digit
        count += 1
    return result

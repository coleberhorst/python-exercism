letter_values = {}
for key, value in {
            "AEIOULNRST": 1,
            "DG": 2,
            "BCMP": 3,
            "FHVWY": 4,
            "K": 5,
            "JX": 8,
            "QZ": 10
            }.items():
    letter_values.update({x : value for x in key})

def score(word):
    return sum([letter_values[x] for x in word.upper()])

def is_pangram(sentence):
    for letter in "abcdefghijklmnopqrstuvwxyz":
        if letter not in sentence:
            return False
    return True

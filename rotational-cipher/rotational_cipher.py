import string


alphabet = string.ascii_lowercase


def rotate(text, key):
    rotated_alphabet = alphabet[key:] + alphabet[:key]
    trans = str.maketrans(alphabet + string.ascii_uppercase, rotated_alphabet + rotated_alphabet.upper())
    return text.translate(trans)

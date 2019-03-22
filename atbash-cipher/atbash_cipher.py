from string import ascii_lowercase
from re import sub

atbash = str.maketrans(ascii_lowercase, ascii_lowercase[::-1])
un_atbash = str.maketrans(ascii_lowercase[::-1], ascii_lowercase)


def encode(plain_text):
    plain_text = sub(r'\W', '', plain_text).lower()
    plain_text = " ".join([plain_text[i:i+5] for i in range(0, len(plain_text), 5)])
    return plain_text.translate(atbash)


def decode(ciphered_text):
    ciphered_text = ciphered_text.replace(" ", "")
    return ciphered_text.translate(un_atbash)

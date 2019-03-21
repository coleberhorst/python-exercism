import re

def verify(isbn):
    isbn = re.sub("[-A-WY-Z]", "", isbn)
    if len(isbn) > 10 or len(isbn) < 10:
        return False
    value = 0
    for i in range(len(isbn)):
        if isbn[i] != "X":
            value += (10-i) * int(isbn[i])
    value += (isbn[9] == "X") * 10
    return value % 11 == 0

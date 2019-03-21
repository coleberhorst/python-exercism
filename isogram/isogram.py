def is_isogram(string):
    string = list(filter(str.isalpha, string.lower()))
    return len(set(string)) == len(string)

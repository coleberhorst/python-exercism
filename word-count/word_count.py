import re

def word_count(phrase):
    frequency = {}
    phrase = re.sub("[^a-zA-Z0-9' ]+", ' ', phrase)
    for word in phrase.split():
        word  = word.lower().strip("\'")
        if word in frequency:
            frequency[word] = frequency[word] + 1
        else:
            frequency[word] = 1
    return frequency

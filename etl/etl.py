def transform(legacy_data):
    return {letter.lower(): score for score, letter in legacy_data.items() for letter in letter}

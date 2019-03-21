def abbreviate(words):
    words = words.replace("-", " ").replace("_", " ")
    return "".join([x[0].capitalize() for x in words.split()])

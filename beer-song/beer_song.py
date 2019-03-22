def recite(start, take=1):
    lyrics, stop = [], start - take
    while start >= 0 and start != stop:
        lyrics.extend(verse(start))
        start -= 1
        if start != stop:
            lyrics.append("")
    return lyrics


def verse(count):
    it_one = (count == 1) * "it" + (count > 1) * "one"
    b1 = (count == 0) * "No more" + (count > 0) * str(count)
    b2 = (count == 0) * "no more" + (count > 0) * str(count)
    action = (count == 0) * "Go to the store and buy some more, " + \
        (count > 0) * ("Take " + it_one + " down and pass it around, ")
    b3 = (count == 1) * "no more" + (count > 1) * str(count - 1) + (count == 0) * str(99)
    s1 = (count > 1 or count == 0) * "s"
    s2 = (count > 2 or count <= 1) * "s"
    return [b1 + " bottle" + s1 + " of beer on the wall, " + b2 + " bottle" + s1 + " of beer.",
            action + b3 + " bottle" + s2 + " of beer on the wall."]

def decode(string):
    result, count = "", 0
    for i, char in enumerate(string):
        if char.isdigit():
            if count > 10:
                continue
            count = int(char)
            if string[i+1].isdigit():
                count *= 10
                count += int(string[i+1])
        elif (char.isalpha() or char == " ") and not count:
            result += char
        elif count:
            result += char * count
            count = 0
    return result


def encode(string):
    if not string:
        return ""
    frequency = [(0, string[0])]
    for char in string:
        if char == frequency[-1][1]:
            frequency[-1] = (frequency[-1][0] + 1, char)
        else:
            frequency.append((1, char))
    return "".join([str(x[0]) + x[1] if x[0] > 1 else x[1] for x in frequency])

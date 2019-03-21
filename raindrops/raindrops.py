def raindrops(number):
    output = (number % 3 == 0)*"Pling" + (number % 5 == 0)*"Plang" +  (number % 7 == 0)*"Plong"
    if not output:
        return str(number)
    else:
        return output

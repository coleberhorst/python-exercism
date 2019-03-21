def binary_search(list_of_numbers, number):
    first, last = 0, len(list_of_numbers) - 1
    while first <= last:
        half = (first + last) // 2
        if list_of_numbers[half] == number:
            return half
        elif number < list_of_numbers[half]:
            last = half - 1
        elif number > list_of_numbers[half]:
            first = half + 1
    raise ValueError("Number not found.")

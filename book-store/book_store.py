from collections import defaultdict

BOOK_PRICES = [0, 800, 1520, 2160, 2560, 3000]


def calculate_total(books):
    count = defaultdict(int)
    for b in books:
        count[b] += 1
    largest_set, price = len(set(books)), 0

    while sum(count.values()):
        subtract_counter = largest_set
        print(largest_set, subtract_counter, count)
        for b in count:
            if count[b] > 0 and subtract_counter > 0:
                subtract_counter -= 1
                count[b] -= 1
        price += BOOK_PRICES[largest_set - subtract_counter]
        print(largest_set, subtract_counter, count, price)
    return price
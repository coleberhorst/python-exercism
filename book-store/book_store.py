from collections import OrderedDict, defaultdict
from operator import itemgetter

BOOK_PRICES = [0, 800, 1520, 2160, 2560, 3000]


def calculate_total(books):
    count = defaultdict(int)
    for b in books:
        count[b] += 1
    largest_set, set_results = len(set(books)), [0]*6
    if not largest_set:
        return 0

    for i in range(1, largest_set + 1):
        temp_count = OrderedDict(sorted(count.items(), key=itemgetter(1), reverse=True))
        price = 0
        while sum(temp_count.values()):
            subtract_counter = i
            for b in temp_count:
                if temp_count[b] > 0 and subtract_counter > 0:
                    subtract_counter -= 1
                    temp_count[b] -= 1
            price += BOOK_PRICES[i - subtract_counter]
        set_results[i] = price
    return min(x for x in set_results if x > 0)
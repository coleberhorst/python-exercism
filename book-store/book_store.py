discounts = {1:1, 2:.95, 3:.9, 4:.8, 5:.75}


def calculate_total(books):
    # take a list of books 1-5, might be duplicates
    # split into discount groups, minimizing the number of alone books 4, 4 is better than 3,5
    book_sets = [[]]*10
    print(book_sets)
    for b in books:
        i = 0
        while i != 10 and b in book_sets[i] :
            i += 1
        book_sets[i].append(b)
    print(book_sets)

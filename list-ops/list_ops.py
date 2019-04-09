def append(xs, ys):
    return xs + ys


def concat(lists):
    return list([item for group in lists for item in group])


def filter_clone(function, xs):
    return [i for i in xs if function(i)]


def length(xs):
    l = 0
    for i in xs:
        l += 1
    return l


def map_clone(function, xs):
    return [function(i) for i in xs]


def foldl(function, xs, acc):
    total = acc
    for i in xs:
        total = function(i, total) if total != 0 else total
    return total


def foldr(function, xs, acc):
    total = acc
    for i in reverse(xs):
        total = function(i, total) if total != 0 else total
    return total


def reverse(xs):
    return xs[::-1]

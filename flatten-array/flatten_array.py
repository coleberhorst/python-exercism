def flatten(iterable):
    result = []
    for i in range(len(iterable)):
        if iterable[i] is not None and isinstance(iterable[i], (list,)):
            iterable = flatten(iterable[i]).extend(iterable[i+1:])
        else:
            result.append(i)
    return result

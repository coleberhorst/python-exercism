def sum_of_multiples(limit, multiples):
    list_pool = []
    for m in multiples:
        if m:
            list_pool.extend([x for x in range(m, limit, m)])
    return sum(set(list_pool))

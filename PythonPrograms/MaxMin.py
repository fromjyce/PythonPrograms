def max_min(lst):
    return_lst = []
    while lst:
        max_n = max(lst)
        return_lst.append(max_n)
        lst.remove(max_n)

        if not lst:
            break

        min_n = min(lst)
        return_lst.append(min_n)
        lst.remove(min_n)

    return return_lst

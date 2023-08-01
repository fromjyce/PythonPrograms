def right_rotate(lst, k):
    if not lst or k == 0:
        return lst

    k %= len(lst)
    return lst[-k:] + lst[:-k]

#Give an integer list, return the maximum sublist sum. the list may contain both positive and negative integers and is unsorted
def max_sublist_sum(lst):
    if not lst:
        return 0

    current_sum = lst[0]
    max_sum = lst[0]

    for num in lst[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum

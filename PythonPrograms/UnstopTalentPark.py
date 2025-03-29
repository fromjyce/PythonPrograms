def min_items_to_buy(s1, s2, s3, s4):
    unique_colors = len(set([s1, s2, s3, s4]))
    return 4 - unique_colors


s1 = int(input().strip())
s2 = int(input().strip())
s3 = int(input().strip())
s4 = int(input().strip())


print(min_items_to_buy(s1, s2, s3, s4))

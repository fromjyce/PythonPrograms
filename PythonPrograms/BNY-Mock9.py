def find_min_cards(c):
    sum_h = 0.0
    n = 0
    while sum_h < c:
        n += 1
        sum_h += 1 / (n + 1)
    return n

def main():
    while True:
        try:
            value = input().strip()
            c = float(value)
            if c == 0.00:
                break
            result = find_min_cards(c)
            print(f"{result} card(s)")
        except ValueError:
            # Handle invalid input, though not expected per problem constraints
            continue

if __name__ == "__main__":
    main()

import math


def is_perfect_square(num):
    root = int(math.sqrt(num))
    return root * root == num


def count_perfect_pairs(arr):
    n = len(arr)
    count = 0

    for i in range(n):
        for j in range(i + 1, n):
            product = arr[i] * arr[j]
            if is_perfect_square(product):
                count += 1

    return count


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        result = count_perfect_pairs(a)
        print(result)


if __name__ == "__main__":
    main()

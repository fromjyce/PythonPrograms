"""
Best Bubble
Problem Description
Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in the wrong order. The problem with bubble sort is its worst case scenario. When the smallest element is in the last position, then it takes more time to sort in ascending order, but takes less time to sort in descending order.

An array is called beautiful if all the elements of the array are in either ascending or descending order. Given an array of numbers, find the minimum swap operations required to make the array beautiful.

Constraints
0 < N < 1000

0 < Arr[i] < 1000

Input
First line contains of integer N denoting number of elements in the array.

Second line consist of N integers separated by space denoting the elements of the array.

Output
Single integer denoting the least numbers of swap operations required to make the array beautiful.

Time Limit (secs)
1

Examples
Example 1

Input

5

4 5 3 2 1

Output

1

Explanation

The number of swaps required to sort the elements in ascending order is 9.

The number of swaps required to sort the elements in descending order is 1.

The best way is to sort in descending order and swaps required is 1.

Example 2

Input

5

4 5 1 2 3

Output

4

Explanation

Ascending order:

Pass/Index

a

b

c

d

e

Comparison

Need swap

Swap count

Pass 1

4

5

1

2

3

a b

No

0

4

5

1

2

3

b c

Yes

1

4

1

5

2

3

c d

Yes

2

4

1

2

5

3

d e

Yes

3

Pass 2

4

1

2

3

5

a b

Yes

4

1

4

2

3

5

b c

Yes

5

1

2

4

3

5

c d

Yes

6

1

2

3

4

5

d e

No

6

Descending order:

Pass/index

a

b

c

d

e

Comparison

Need swap

Swap count

Pass 1

4

5

1

2

3

a b

Yes

1

5

4

1

2

3

b c

No

1

5

4

1

2

3

c d

Yes

2

5

4

2

1

3

d e

Yes

3

Pass 2

5

4

2

3

1

a b

No

3

5

4

2

3

1

b c

No

3

5

4

2

3

1

c d

yes

4

5

4

3

2

1

d e

No

4

The number of swaps required to sort the elements in ascending order is 6.

The number of swaps required to sort the elements in descending order is 4.

The best way is to sort in descending order and swaps required is 4.
"""


def bubble_sort_swaps(arr, order):
    n = len(arr)
    swaps = 0

    for i in range(n):
        for j in range(0, n - i - 1):
            if (order == "ascending" and arr[j] > arr[j + 1]) or (
                order == "descending" and arr[j] < arr[j + 1]
            ):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1

    return swaps


def min_swaps_to_beautiful_array(arr):
    asc_swaps = bubble_sort_swaps(arr.copy(), "ascending")
    desc_swaps = bubble_sort_swaps(arr.copy(), "descending")

    return min(asc_swaps, desc_swaps)


# Example usage:
n = int(input())
arr = list(map(int, input().split()[:n]))

result = min_swaps_to_beautiful_array(arr)
print(result)

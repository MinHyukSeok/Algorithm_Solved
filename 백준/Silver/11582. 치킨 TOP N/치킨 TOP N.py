import sys
import math
sys.setrecursionlimit(10**5)


def merge(arr, c):
    if c == 0 or len(arr) == 1:
        return sorted(arr)

    middle = len(arr) // 2
    left = merge(arr[:middle], c - 1)
    right = merge(arr[middle:], c - 1)
    res = left + right
    return res


N = int(input())
lst = list(map(int, input().split()))
k = int(input())

r = merge(lst, int(math.log2(k)))
print(*r)

# print(int(math.log2(1)))
# print(merge(lst, int(math.log2(1))))
import sys
import math
sys.setrecursionlimit(10**5)


def merge(arr, c):
    if c == 0 or len(arr) == 1:             # 합칠때 정렬
        return sorted(arr)

    middle = len(arr) // 2                  # 분해
    left = merge(arr[:middle], c - 1)
    right = merge(arr[middle:], c - 1)
    res = left + right
    return res


N = int(input())
lst = list(map(int, input().split()))
k = int(input())

r = merge(lst, int(math.log2(k)))
print(*r)

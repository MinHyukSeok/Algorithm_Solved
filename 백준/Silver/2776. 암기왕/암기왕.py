import sys
from collections import deque

input = sys.stdin.readline

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    lst_1 = list(map(int, input().split()))
    M = int(input())
    lst_2 = deque(map(int, input().split()))

    lst_1.sort()

    while lst_2:
        num = lst_2.popleft()
        start = 0
        end = N - 1
        res = 0
        while start <= end:
            middle = (start + end) // 2

            if num == lst_1[middle]:
                res = 1
                break
            elif num > lst_1[middle]:
                start = middle + 1
            elif num < lst_1[middle]:
                end = middle - 1
        print(str(res))



# 1 2 3 4 5

# 1 3 7 9 5
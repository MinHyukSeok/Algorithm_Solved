import sys
from itertools import combinations

sys.setrecursionlimit(10 ** 6)


# def recur(s, i, k):
#     global cnt
#
#     if k and s == S:
#         cnt += 1
#
#     if i == N:
#         return
#
#     recur(s + lst[i], i + 1, k + 1)
#     recur(s, i + 1, k)


N, S = map(int, input().split())
lst = list(map(int, input().split()))
cnt = 0

arr = []

for i in range(1, N + 1):
    for l in list(combinations(lst, i)):
        if sum(l) == S:
            cnt += 1
print(cnt)

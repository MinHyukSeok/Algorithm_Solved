from collections import deque

n, m = map(int, input().split())

lst = list(map(int, input().split()))

res = 0
sum_n = 0

for i in range(m):
    sum_n += lst[i]

res = sum_n

for i in range(m, n):
    sum_n += lst[i]
    sum_n -= lst[i - m]

    if sum_n > res:
        res = sum_n

print(res)
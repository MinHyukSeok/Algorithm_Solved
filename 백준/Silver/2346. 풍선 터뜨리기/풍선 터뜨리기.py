from collections import deque

n = int(input())

dict = []
res = []
lst = list(map(int, input().split()))

for i in range(len(lst)):
    dict.append((i + 1, lst[i]))
idx = 0

for i in range(n):
    t = dict.pop(idx)
    res.append(t[0])
    if len(dict) == 0:
        break
    elif len(dict) == 1:
        t = dict.pop()
        res.append(t[0])
        break
    elif t[1] > 0:
        idx += abs(t[1] - 1)
        idx = idx % len(dict)
    else:
        idx -= abs(t[1])
        idx = idx % len(dict)

print(*res)
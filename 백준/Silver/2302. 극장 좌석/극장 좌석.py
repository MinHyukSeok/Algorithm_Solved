lst = [1, 1, 2, 3, 5, 8]

from collections import deque

def case_count(fn):
    global lst
    if fn <= len(lst) - 1:
        return lst[fn]
    else:
        while fn != len(lst) - 1:
            lst.append((lst[-1] + lst[-2]))
        return lst[fn]


N = int(input())
M = int(input())
vip_list = deque()

for _ in range(M):
    vip_list.append(int(input()))

start = 1
end = N
res = 1

while vip_list:
    idx = vip_list.popleft()
    res = res * case_count(idx - start)
    start = idx + 1

res = res * case_count(end - start + 1)

print(res)
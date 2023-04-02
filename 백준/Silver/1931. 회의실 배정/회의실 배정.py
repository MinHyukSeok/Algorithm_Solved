import sys

N = int(input())
lst = []
for _ in range(N):
    start, end = map(int, sys.stdin.readline().split())
    lst.append([start, end])

lst.sort(key=lambda x: (x[1], x[0]))

start = lst[0][1]
cnt = 1
for i in range(1, N):
    if lst[i][0] >= start:
        cnt += 1
        start = lst[i][1]

print(cnt)
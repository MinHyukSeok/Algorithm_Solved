import sys
input = sys.stdin.readline
print = sys.stdout.write


N, Q = map(int, input().split())

lst = list(map(int, input().split()))
lst.sort()

for i in range(1, N):
    lst[i] = lst[i] + lst[i - 1]

for i in range(Q):
    a, b = map(int, input().split())
    if a > 1:
        print(str(lst[b - 1] - lst[a - 2]) + "\n")
    elif a <= 1:
        print(str(lst[b - 1]) + "\n")
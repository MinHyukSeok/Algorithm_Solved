N = int(input())
distance = list(map(int, input().split()))
charge = list(map(int, input().split()))
res = charge[0] * distance[0]
cur = charge[0]

for i in range(1, N - 1):
    if cur > charge[i]:
        cur = charge[i]
    res += (cur * distance[i])

print(res)
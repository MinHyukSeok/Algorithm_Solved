def recur(idx, lst):
    global N
    if idx == len(t):
        if len(lst) == N // 2:
            res.append(lst[:])
        return
    lst.append(t[idx])
    recur(idx+1, lst)
    lst.pop()
    recur(idx+1, lst)


N = int(input())
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))
t = [x for x in range(1, N + 1)]
res = []
recur(0, [])
left = 0
right = len(res) - 1
minN = 1000000000
while left < right:
    team1 = res[left]
    team2 = res[right]
    stats1 = 0
    stats2 = 0
    for i in team1:
        for j in team1:
            if i != j:
                stats1 += arr[i-1][j-1]
    for i in team2:
        for j in team2:
            if i != j:
                stats2 += arr[i-1][j-1]

    if abs(stats1 - stats2) < minN:
        minN = abs(stats1 - stats2)
    left += 1
    right -= 1

print(minN)
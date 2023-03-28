import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
cnt_arr = [0] * 10001
maxN = 0
minN = 10000
for _ in range(N):
    idx = int(input())
    cnt_arr[idx] += 1
    if idx > maxN:
        maxN = idx
    elif idx < minN:
        minN = idx

for i in range(minN, maxN + 1):
    if cnt_arr[i] >= 1:
        for _ in range(cnt_arr[i]):
            print(f'{i}\n')
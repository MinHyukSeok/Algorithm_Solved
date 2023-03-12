from collections import deque
import sys

dxy = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 북동남서


def move(fx, fy, d):
    fx = fx + dxy[d][0]
    fy = fy + dxy[d][1]

    return fx, fy


M, N = map(int, sys.stdin.readline().rstrip().split())

arr = []
q = deque()
arr.append([-1] * (M + 2))
for i in range(N):
    arr.append([-1] + list(map(int, sys.stdin.readline().rstrip().split())) + [-1])
    for j in range(1, M + 1):
        if arr[i + 1][j] == 1:
            q.append((i + 1, j))            # 토마토 들어있는 칸 좌표 찾기
arr.append([-1] * (M + 2))


while q:
    cx, cy = q.popleft()
    for i in range(4):
        x, y = move(cx, cy, i)
        if arr[x][y] == 0:
            q.append((x, y))
            arr[x][y] = arr[cx][cy] + 1

res = max(map(max, arr)) - 1

for m in range(1, N + 1):
    if arr[m].count(0) >= 1:
        res = -1
        break

print(str(res))
import copy

dxy = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def move(fx, fy, fd):

    fx = fx + dxy[fd][0]
    fy = fy + dxy[fd][1]

    return fx, fy


N = int(input())
stack = []
arr = [list(map(int, input().split())) for _ in range(N)]

res = 0
max_n = 0

for m in arr:
    if max(m) > max_n:
        max_n = max(m)

while max_n:
    cnt = 0
    temp_arr = copy.deepcopy(arr)
    visited = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if temp_arr[i][j] < max_n:
                temp_arr[i][j] = 0

    for i in range(N):
        for j in range(N):
            v = 1
            if temp_arr[i][j] >= 1 and visited[i][j] == 0:
                cnt += 1
                stack.append((i, j))
                visited[i][j] = v
                v += 1
            while stack:
                cx, cy = stack.pop()
                for d in range(4):
                    x, y = move(cx, cy , d)
                    if 0 <= x < N and 0 <= y < N:
                        if visited[x][y] == 0 and temp_arr[x][y] >= 1:
                            stack.append((x, y))
                            visited[x][y] = v
                            v += 1

    if cnt > res:
        res = cnt
    max_n -= 1

print(res)
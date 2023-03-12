import copy

dxy = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def move(fx, fy, fd):

    fx = fx + dxy[fd][0]
    fy = fy + dxy[fd][1]

    return fx, fy


N = int(input())
stack = []
arr = [list(input()) for _ in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)]


cnt = 0
res = []
for i in range(N):
    for j in range(N):
        v = 0
        if arr[i][j] == '1' and visited[i][j] == 0:
            cnt += 1
            stack.append((i, j))
            v += 1
            visited[i][j] = v
        while stack:
            cx, cy = stack.pop()
            for d in range(4):
                x, y = move(cx, cy , d)
                if 0 <= x < N and 0 <= y < N:
                    if visited[x][y] == 0 and arr[x][y] == '1':
                        stack.append((x, y))
                        v += 1
                        visited[x][y] = v
        if v != 0:
            res.append(v)

res.sort()
print(cnt)
for i in res:
    print(i)
dxy = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def move(fx, fy, fd):

    fx = fx + dxy[fd][0]
    fy = fy + dxy[fd][1]

    return fx, fy


N, M = map(int, input().split())
stack = []
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]
cnt = 0

for i in range(N):
    for j in range(M):
        v = 1
        if arr[i][j] == 1 and visited[i][j] == 0:
            cnt += 1
            stack.append((i, j))
            visited[i][j] = v
            v += 1
        while stack:
            cx, cy = stack.pop()
            for d in range(4):
                x, y = move(cx, cy , d)
                if 0 <= x < N and 0 <= y < M:
                    if visited[x][y] == 0 and arr[x][y] == 1:
                        stack.append((x, y))
                        visited[x][y] = v
                        v += 1

max_n = 0

for m in visited:
    if max(m) > max_n:
        max_n = max(m)

print(cnt)
print(max_n)

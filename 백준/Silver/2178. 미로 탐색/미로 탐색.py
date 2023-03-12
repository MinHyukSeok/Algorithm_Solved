dxy = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 북동남서


def move(fx, fy, d):
    fx = fx + dxy[d][0]
    fy = fy + dxy[d][1]

    return fx, fy


N, M = map(int, input().split())
arr = []
q = []
arr.append([0] * (M + 2))
for i in range(N):
    arr.append([0] + list(map(int, list(input()))) + [0])   # 미로 입력 및 0로 패딩
    # for j in range(1, N + 1):                               # 입력과 동시에 시작점 위치 찾기
    #     if arr[i + 1][j] == 2:
    #         start_x = i + 1
    #         start_y = j
arr.append([0] * (M + 2))


visited = [[0 for _ in range(M + 2)] for _ in range(N + 2)]
visited[1][1] = 1
q.append([1, 1])
res = 0
success = 0
while q:
    cx, cy = q.pop(0)
    for i in range(4):
        x, y = move(cx, cy, i)
        if arr[x][y] != 0 and visited[x][y] == False:
            q.append([x, y])
            visited[x][y] = visited[cx][cy] + 1
        if x == N and y == M:
            success = 1
            res = max(map(max, visited))
            break
    if success == 1:
        break


print(f'{res}')

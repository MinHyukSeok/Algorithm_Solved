dxy = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 북동남서

def move(fx, fy, d):
    fx = fx + dxy[d][0]
    fy = fy + dxy[d][1]

    return fx, fy

M, N = map(int, input().split())

arr = [[0] * (M + 2)] + [[0] + list(input()) + [0] for _ in range(N)] + [[0] * (M + 2)]

q = []

resW = []
resB = []


visited = [[0 for _ in range(M + 2)] for _ in range(N + 2)]

for start_x in range(1, N + 1):
        for start_y in range(1, M + 1):
            cnt = 1
            sx, sy = start_x, start_y

            if arr[start_x][start_y] == 'W' and visited[start_x][start_y] == 0:
                visited[start_x][start_y] = 1
                q.append([start_x,start_y])

                while q:
                    on_off = 0                  # 탐색 여부
                    cx, cy = q.pop(0)

                    for i in range(4):
                        x, y = move(cx, cy, i)

                        if arr[x][y] == 'W' and visited[x][y] == False:
                            q.append([x, y])
                            visited[x][y] = 1
                            on_off = 1          # 탐색 됨
                            cnt += 1

                if on_off == 0:                 # 탐색이 되지 않았다면 끝점
                    resW.append(cnt)

            cnt = 1
            sx, sy = start_x, start_y

            if arr[start_x][start_y] == 'B' and visited[start_x][start_y] == 0:
                visited[start_x][start_y] = 1
                q.append([start_x,start_y])

                while q:
                    on_off = 0                  # 탐색 여부
                    cx, cy = q.pop(0)

                    for i in range(4):
                        x, y = move(cx, cy, i)

                        if arr[x][y] == 'B' and visited[x][y] == False:
                            q.append([x, y])
                            visited[x][y] = 1
                            on_off = 1          # 탐색 됨
                            cnt += 1

                if on_off == 0:                 # 탐색이 되지 않았다면 끝점
                    resB.append(cnt)


r1 = 0
r2 = 0
for i in resW:
    r1 += (i ** 2)
for i in resB:
    r2 += (i ** 2)

print(r1, r2)
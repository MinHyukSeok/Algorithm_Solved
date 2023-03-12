dx = [-1, 0 , 1, 0]        # 12시부터 시계 방향으로
dy = [0, 1, 0 , -1]


def move(fx, fy, fd):                   # 이동 함수 (출발 좌표, 이동 방향 입력 받음)
    fcx = fx + dx[fd]
    fcy = fy + dy[fd]

    return fcx, fcy

T = int(input())
for test_case in range(1, T + 1):

    w, h, n = map(int, input().split())             # 배추밭 가로 세로길이, 배추 수 입력


    arr = [[0] * (w + 2) for _ in range(h + 2)]
    for i in range(n):
        a , b = map(int, input().split())
        arr[b + 1][a + 1] = 1

    stack = []

    res_cnt = 0

    for i in range(1, h + 1):
        for j in range(1, w + 1):
            if arr[i][j] == 1:                      # 섬인 경우
                res_cnt += 1                        # 카운팅
                arr[i][j] = 0                       # 해당 자리 0으로
                stack.append((i, j))                # 해당 좌표 스택에 추가
                while stack:
                    cx, cy = stack.pop()            # 스택에 있는 좌표 하나 빼서
                    for d in range(4):              # 주변 탐색
                        x, y = move(cx, cy, d)      # 11시부터 시계방향으로 이동
                        if arr[x][y] == 1:          # 섬인 경우
                            arr[x][y] = 0           # 해당 자리 0으로
                            stack.append((x, y))    # 해당 좌표 스택에 추가

    print(res_cnt)

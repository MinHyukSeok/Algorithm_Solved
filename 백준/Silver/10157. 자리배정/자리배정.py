import sys
input = sys.stdin.readline
print = sys.stdout.write


dxy = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 북동남서


def move(fx, fy, fd):
    fx = fx + dxy[fd][0]
    fy = fy + dxy[fd][1]

    return fx, fy


i, j = map(int, input().split())  # 배열 크기

k = int(input())                  # k번째 좌표 찾기

arr = [[0] * i for _ in range(j)]
visited = [[0] * i for _ in range(j)]

start_x = j - 1                   # 왼쪽 아래부터 출발
start_y = 0
stack = []

stack.append([start_x, start_y])

visited[start_x][start_y] = 1
d = 0
res = 0
if 2 <= k < i * j + 1:
    while stack:
        x, y = stack.pop()
        cx, cy = move(x, y, d % 4)

        if 0 <= cx < j and 0 <= cy < i:        # 범위 설정
            if visited[cx][cy] == 0:
                stack.append([cx, cy])
                visited[cx][cy] = visited[x][y] + 1

                if visited[cx][cy] == k:                                    # k번째 좌석번호라면
                    res = [cx, cy]
                    break
            else:
                stack.append([x, y])
                d += 1
        else:                                                           # 범위를 벗어나면 이동 방향 회전
            stack.append([x, y])
            d += 1

    if res != 0:
        q = str(res[1] + 1) + ' ' + str(j - res[0])
        print(q)
    else:
        print('0')

elif k == 1:
    # q = str(start_y + 1) + ' ' + str(j - start_x)
    q = '1 1'
    print(q)

else:
    print('0')
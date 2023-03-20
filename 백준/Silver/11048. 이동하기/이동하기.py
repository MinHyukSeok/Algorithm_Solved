from collections import deque
import sys
input = sys.stdin.readline
print = sys.stdout.write


dxy = [(1, 0), (0, 1), (1, 1)]

def move(fx, fy, fd):
    fx = fx + dxy[fd][0]
    fy = fy + dxy[fd][1]

    return fx, fy

def move_r(fx, fy, fd):
    fx = fx - dxy[fd][0]
    fy = fy - dxy[fd][1]

    return fx, fy



N, M = map(int,input().split())

arr = []

for i in range(N):
    arr.append(list(map(int, input().split())))

visited = [[False for _ in range(M)] for _ in range(N)]

stack = deque()

stack.append((0, 0))

visited[0][0] = True

n_list = []

while stack:
    sx, sy = stack.popleft()

    for d in range(3):
        cx, cy = move(sx, sy, d)
        if 0 <= cx < N and 0 <= cy < M and visited[cx][cy] == False:
            stack.append((cx, cy))

            max_n = 0

            for r in range(3):
                rx, ry = move_r(cx, cy, r)

                if 0 <= rx < N and 0 <= ry < M and arr[rx][ry] > max_n:
                    max_n = arr[rx][ry]

            arr[cx][cy] += max_n
            visited[cx][cy] = True


print(str(arr[N - 1][M - 1]))

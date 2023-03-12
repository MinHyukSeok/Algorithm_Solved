import copy

dxy = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def move(fx, fy, fd):

    fx = fx + dxy[fd][0]
    fy = fy + dxy[fd][1]

    return fx, fy

wolf = merry = 0
C, R = map(int,input().split())
stack = []
arr = [list(input()) for _ in range(C)]
visited = [[0 for _ in range(R)] for _ in range(C)]


cnt = 0
res = []
for i in range(C):
    for j in range(R):
        v = 0
        temp = []
        if arr[i][j] != '#' and visited[i][j] == 0:
            cnt += 1
            stack.append((i, j))
            v += 1
            visited[i][j] = v
            temp.append(arr[i][j])
        while stack:
            cx, cy = stack.pop()
            for d in range(4):
                x, y = move(cx, cy , d)
                if 0 <= x < C and 0 <= y < R:
                    if visited[x][y] == 0 and arr[x][y] != '#':
                        stack.append((x, y))
                        v += 1
                        visited[x][y] = v
                        temp.append(arr[x][y])


        if temp.count('o') > temp.count('v'):
            merry += temp.count('o')
        else:
            wolf += temp.count('v')



print(merry, wolf)
dxy = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def move(fx, fy, fd):
    fx = fx + dxy[fd][0]
    fy = fy + dxy[fd][1]

    return fx, fy


def change(fs):                 # 5진수로 변환
    res = ''
    if fs == ' ':
        return '00000'
    else:
        fs = ord(fs) - 64

        while fs:
            if fs >= 16:
                fs -= 16
                res += '1'
            else:
                res += '0'

            if fs >= 8:
                fs -= 8
                res += '1'
            else:
                res += '0'

            if fs >= 4:
                fs -= 4
                res += '1'
            else:
                res += '0'

            if fs >= 2:
                fs -= 2
                res += '1'
            else:
                res += '0'

            if fs >= 1:
                fs -= 1
                res += '1'
            else:
                res += '0'

    return res



T = int(input())
for test_case in range(1, T + 1):
    C, R, *S = map(str, input().split(' '))
    arr = [[0 for _ in range(int(R))] for _ in range(int(C))]
    visited = [[0 for _ in range(int(R))] for _ in range(int(C))]

    stack = []
    start_x = start_y = 0

    r = ''
    S = list(' '.join(S))
    for i in S:
        r+= change(i)

    r = list(r)

    if len(r) == 0:
        print('0' * (int(R) * int(C)))
    else:
        arr[0][0] = r.pop(0)
        stack.append((0, 0))
        visited[0][0] = 1

        d = 1
        cnt = 1
        while stack:
            if cnt == int(R) * int(C):
                break
            sx, sy = stack.pop(0)
            cx, cy = move(sx, sy, d % 4)
            if 0<=cy<int(R) and 0<=cx<int(C) and visited[cx][cy] == 0:
                if len(r) == 0:
                    arr[cx][cy] == '0'
                else:
                    arr[cx][cy] = r.pop(0)

                stack.append((cx,cy))
                visited[cx][cy] = 1
                cnt += 1
            else:
                d += 1
                stack.insert(0, (sx, sy))

        res = ''

        for i in range(int(C)):
            for j in range(int(R)):
                res += str(arr[i][j])

        print(res)



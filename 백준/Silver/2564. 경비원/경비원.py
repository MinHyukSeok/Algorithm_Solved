M, N = map(int, input().split())

l = int(input())

lst = []
res = 0
for i in range(l + 1):
    a, b = map(int, input().split())
    if a == 1:                      # 북
        a, b, c = 0, b, 1
    elif a == 2:                    # 남
        a, b, c = N, b, 3
    elif a == 3:                    # 서
        a, b, c = b, 0, 4
    elif a == 4:                    # 동
        a, b, c = b, M, 2

    lst.append((a, b, c))

start_x , start_y, start_d = lst.pop()

while lst:
    x, y, d = lst.pop()
    if d == start_d:                                        # 동일 선상인 경우
        res += (abs(x - start_x) + abs(y - start_y))

    elif abs(d - start_d) == 2:                             # 반대에 있는 경우
        if d == 1 or d == 3:                                # 북쪽, 남쪽인 경우
            temp1 = start_y + y + N                         # 왼쪽으로 돌기
            temp2 = (M - y) + (M - start_y) + N             # 오른쪽으로 돌기
            res += min(temp1, temp2)                        # 가까운거리 ++

        elif d == 2 or d == 4:                              # 동쪽, 서쪽인 경우
            temp1 = start_x + x + M                         # 왼쪽으로 돌기
            temp2 = (N - x) + (N - start_x) + M             # 오른쪽으로 돌기
            res += min(temp1, temp2)                        # 가까운거리 ++

    else:                                                   # 인접한 경우
        res += (abs(start_x - x) + abs(start_y - y))
print(res)
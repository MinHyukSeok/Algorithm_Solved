T = int(input())

for test_case in range(T):
    H, W, N = map(int, input().split())

    row = N % H
    col = N // H + 1

    if row == 0:
        row = H
        col -= 1

    if col < 10:
        col = '0' + str(col)


    print(str(row) + str(col))

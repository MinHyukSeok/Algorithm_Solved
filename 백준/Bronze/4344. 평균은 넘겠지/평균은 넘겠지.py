T = int(input())

for test_case in range(1, T + 1):
    cnt = 0
    N, *lst = map(int, input().split())
    average = sum(lst) / N

    for i in lst:
        if average < i:
            cnt += 1

    res = cnt / N * 100

    res = str(round(res, 3))
    while 1:
        if float(res) >= 10:
            if len(res) != 6:
                res += '0'
            else:
                break
        else:
            if len(res) != 5:
                res += '0'
            else:
                break

    res += '%'

    print(str(res))

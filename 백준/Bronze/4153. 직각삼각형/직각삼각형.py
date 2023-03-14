while 1:
    triangle_len = list(map(int, input().split()))
    if triangle_len[0] == 0:
        break
    else:
        max_len = max(triangle_len)
        check1 = 0
        check2 = 0
        for i in triangle_len:
            if i == max_len:
                check1 += i * i
            else:
                check2 += i * i
    if check1 == check2:
        print('right')
    else:
        print('wrong')


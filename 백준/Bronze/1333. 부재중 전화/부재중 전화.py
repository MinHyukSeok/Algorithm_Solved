N ,L, D = map(int,input().split())

res = 0
cnt = 1
L_cnt = 1
r = L

while N:
    if (D * cnt) - r < 0:
        cnt += 1

    elif (D * cnt) - r < 5:
        break
    else:
        N -= 1
        r += (5 + (L * L_cnt))

print(D * cnt)
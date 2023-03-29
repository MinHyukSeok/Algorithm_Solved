N = int (input())

five_max = N // 5
Three_min = 0
res = -1
on_off = 1
for i in range(five_max, -1, -1):
    for j in range(Three_min, (N - (5 * i)) // 3 + 1):
        if N == (i * 5) + (j * 3):
            res = i + j
            on_off = 0
            break
    if on_off == 0:
        break

print(res)
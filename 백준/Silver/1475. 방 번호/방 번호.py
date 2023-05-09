n = list(input())
lst = [0 for _ in range(10)]
cnt = 0
for num in n:
    lst[int(num)] += 1

while 1:
    if max(lst) <= 0:
        break
    cnt += 1

    for i in range(10):
        lst[i] -= 1

    while lst[6] < 0:
        if lst[9] > 0:
            lst[9] -= 1
            lst[6] += 1
        else:
            break

    while lst[9] < 0:
        if lst[6] > 0:
            lst[6] -= 1
            lst[9] += 1
        else:
            break

print(cnt)
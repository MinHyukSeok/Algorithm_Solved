def j(l):
    r = ''

    for i in l:
        r += str(i)

    return r


N = int(input())

res = 0
for i in range(1, N + 1):
    lst = list(map(int, list(str(i))))

    if sum(lst) + i == N:
        res = j(lst)
        break

print(res)
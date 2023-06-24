N = int(input())

lst = list(map(int, input().split()))

res = [(N + 1) for _ in range(N + 1)]

i = 1
while lst:
    a = lst.pop(0)
    t = 1
    while 1:
        if res[t] < i:
            t += 1

        elif a == 0:
            res[t] = i
            i += 1
            break

        elif res[t] > i:
            a -= 1
            t += 1

res.pop(0)

print(*res)
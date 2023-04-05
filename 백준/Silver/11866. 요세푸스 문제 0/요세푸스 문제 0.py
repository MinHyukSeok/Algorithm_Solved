N, K = map(int, input().split())
t = K - 1
lst = [i for i in range(1, N + 1)]
res = []

while lst:
    for i in range(K - 1):
        lst.append(lst.pop(0))
    res.append(str(lst.pop(0)))

print('<', end='')
print(', '.join(res), end='')
print('>', end='')
N = int(input())
lst = list(input())
res = 0
for i in range(N):
    res += ((ord(lst[i]) - 96) * (31 ** i))

print(res)
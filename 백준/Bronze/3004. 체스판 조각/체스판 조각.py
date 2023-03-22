n = int(input())

arr = [0, 2, 4, 6, 9, 12, 16, 20, 25]

i = 1
add_num = 2
res = 2
while i != n:
    res += add_num
    i += 1
    if i % 2 != 0:
        add_num += 1

print(res)
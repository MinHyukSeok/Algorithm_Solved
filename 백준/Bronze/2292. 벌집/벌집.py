N = int(input())

r = 1

idx = 1

while 1:
    if N <= r:
        break
    else:
        r = r + (6 * idx)
        idx += 1

print(idx)
D, K = map(int, input().split())

switch = 1

for A in range(1, K):
    for B in range(A, K):
        arr = [A, B]
        while 1:
            if len(arr) == D:
                if arr[-1] == K:
                    switch = 0
                break

            arr.append(arr[-1] + arr[-2])

        if switch == 0:
            break
    if switch == 0:
        break

for i in range(2):
    print(arr[i])
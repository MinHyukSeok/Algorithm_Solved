N, M = map(int, input().split())

card_list = list(map(int, input().split()))

min_n = 400000

for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            s = card_list[i] + card_list[j] + card_list[k]

            if abs(M - s) <= min_n:
                if s > M:
                    break
                min_n = abs(M - s)
                t = s


print(t)
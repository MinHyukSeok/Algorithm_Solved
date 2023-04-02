def recur(n, total, arr):
    global max_N
    if n == 2:
        max_N = max(max_N, total)
        return
    for i in range(1, len(arr) - 1):
        lst2 = arr[:i] + arr[i + 1:]
        recur(n - 1, total + (arr[i + 1] * arr[i - 1]), lst2)



N = int(input())
lst = [0] + list(map(int, input().split()))
max_N = 0

recur(N, 0, lst.copy())

print(max_N)
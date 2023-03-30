def check(number, compare):
    idx = 0
    for i in range(len(number) - 1):
        if compare[idx] == '>':
            if not number[i] > number[i + 1]:
                return False
        else:
            if not number[i] < number[i + 1]:
                return False
        idx += 1
    return True


def recur(idx):
    global maxN
    global minN
    if idx == k + 1:
        if check(res, arr):
            a = ''.join(str(s) for s in res)
            if int(a) > maxN:
                maxN = int(a)
            if int(a) < minN:
                minN = int(a)
        # result.append(res[:])
    else:
        for i in range(len(N_list)):
            if visited[i] == 0:
                res[idx] = N_list[i]
                visited[i] = 1
                recur(idx + 1)
                visited[i] = 0


maxN = 0
minN = 100000000000000
k = int(input())
arr = list(input().split())
N_list = [i for i in range(10)]
visited = [0] * 10
res = [0] * (k + 1)
result = []
recur(0)
l = 0

# r = len(result) - 1
# while 1:
#     if check(result[r], arr):
#         print(''.join(str(s) for s in result[r]))
#         break
#     r -= 1
# while 1:
#     if check(result[l], arr):
#         print(''.join(str(s) for s in result[l]))
#         break
#     l += 1

if len(list(str(maxN))) < k + 1:
    maxN = '0'+str(maxN)
if len(list(str(minN))) < k + 1:
    minN = '0'+str(minN)
print(maxN)
print(minN)
def check(l1, l2):
    if l1[0] > l2[0] and l1[1] > l2[1]:             # 첫번째 사람이 더 큰 경우
        return True
    else:                                           # 두사람의 덩치가 같은 경우
        return False


N = int(input())
arr = []
res_arr = [0] * N
for i in range(N):
    w, h = map(int, input().split())
    arr.append([w, h, i])               # 몸무게 , 키, 번호 입력

arr.sort(key=lambda x: (x[0], -x[1]), reverse=True)
# print(arr)

idx = 0
rank = 1
res_arr[arr[idx][2]] = rank
idx += 1

for i in range(N):
    cnt = 1
    for j in range(N):
        if check(arr[j], arr[i]):
            cnt += 1

    res_arr[arr[i][2]] = cnt

print(*res_arr)
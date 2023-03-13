

N = int(input())

lst = []
cnt_arr = [0] * 8002        # 최빈값을 찾기 위해 카운트 배열 선언

b = 0
res = []
sum_lst = 0                 # 산술평균을 구하기 위한 누적합

for i in range(N):
    a = int(input())
    sum_lst += a
    lst.append(a)
    cnt_arr[a] += 1

    if b < cnt_arr[a]:       # 입력과 동시에 최빈값 찾기
        b = cnt_arr[a]
        res.clear()
        res.append(a)
    elif b == cnt_arr[a]:
        res.append(a)

lst.sort()
res.sort()
max_n = max(lst)
min_n = min(lst)

if len(res) >= 2:
    res = res[1]
else:
    res = res[0]

r = sum_lst / N

print(round(sum(lst) / N))
print(lst[int(N / 2)])
print(res)
print(max_n - min_n)
T = int(input())
cnt_arr = [[''] for _ in range(201)]
for tc in range(T):
    a = list(input().split())
    age = a[0]
    name = a[1]
    cnt_arr[int(age)].append(name)

for i in range(201):
    if len(cnt_arr[i]) >= 2:
        cnt_arr[i].pop(0)
        while cnt_arr[i]:
            r = cnt_arr[i].pop(0)
            print(f'{i} {r}')
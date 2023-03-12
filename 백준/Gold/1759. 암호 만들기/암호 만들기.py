def check(arr):         # 모음 검사
    if 'a' in arr:
        return True
    elif 'e' in arr:
        return True
    elif 'i' in arr:
        return True
    elif 'o' in arr:
        return True
    elif 'u' in arr:
        return True
    else:
        return False

def check2(arr):        # 자음 검사
    cnt = 0
    for i in arr:
        if check(i) == False:
            cnt += 1
    if cnt >= 2:
        return True
    else:
        return False

res = []
def bt(i, k):
    global res
    if i == k and check(arr) == True and check2(arr) == True:       # 조건에 부합하는 경우
        res.append(''.join(arr.copy()))
        return
    else:
        for j in range(C):
            if len(arr) == 0:                       # 리스트가 비어있을 경우
                arr.append(lst[j])
                bt(i + 1, k)
                arr.pop()
                
            elif (ord(lst[j]) > ord(arr[-1])):      # 마지막 인덱스 알파벳보다 증가한 경우
                arr.append(lst[j])
                bt(i + 1, k)
                arr.pop()

L, C = map(int, input().split())

lst = list(input().split())
arr = []

bt(0, L)

res.sort(key=lambda x: (x, x[1:]))

for r in res:
    print(r)

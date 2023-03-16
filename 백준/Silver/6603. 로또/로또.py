def recur(length, start):
    if length == 6:
        print(*res)
        return
    else:
        for i in range(start, k):
            res.append(lst[i])
            recur(length + 1, i + 1)
            res.pop()

while 1:
    lst = list(map(int, input().split()))       # 로또 번호 입력 받기
    k = lst.pop(0)                              # 첫번째 값 = 로또의 개수
    if k == 0:
        break
    res = []                                    # 결과값을 넣을 배열 선언

    recur(0, 0)                                 # 현재 결과값 배열의 길이 = 0
                                                # 인덱스 시잠점 = 0
    print()

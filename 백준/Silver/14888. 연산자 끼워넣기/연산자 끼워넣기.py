def fusion(nlist, olist):                   # 숫자 리스트, 연산자 리스트 입력받아서 결과 출력
    global n
    for i in range(n - 1):
        if olist[i] == '+':
            nlist[i + 1] = nlist[i] + nlist[i + 1]
        elif olist[i] == '-':
            nlist[i + 1] = nlist[i] - nlist[i + 1]
        elif olist[i] == '*':
            nlist[i + 1] = nlist[i] * nlist[i + 1]
        elif olist[i] == '/':
            if nlist[i] > 0:
                nlist[i + 1] = nlist[i] // nlist[i + 1]
            else:
                nlist[i + 1] = (abs(nlist[i]) // nlist[i + 1]) * (-1)

    return nlist[-1]


def recur(nlist, idx):
    global n
    global max_num
    global min_num

    if idx == n - 1:
        result_number = fusion(nlist.copy(), temp)
        if result_number > max_num:
            max_num = result_number
        if result_number < min_num:
            min_num = result_number
        return 0

    else:
        for i in range(n - 1):
            if visited[i] == 0:
                temp[idx] = operator_list[i]
                visited[i] = 1
                recur(nlist, idx + 1)
                visited[i] = 0


n = int(input())
visited = [0] * (n - 1)
temp = [0] * (n - 1)
max_num = -1000000001
min_num = 1000000001

num_list = list(map(int, input().split()))
operator = list(map(int, input().split()))
operator_list = list(('+' * operator[0]) + ('-' * operator[1]) + ('*' * operator[2]) + ('/' * operator[3]))

recur(num_list, 0)

print(max_num)
print(min_num)
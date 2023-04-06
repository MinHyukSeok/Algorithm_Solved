dic = {}
N = int(input())
n_list = list(map(int, input().split()))
M = int(input())
m_list = list(map(int, input().split()))

for i in m_list:
    dic[i] = 0

for i in n_list:
    if i in dic:
        dic[i] += 1

for i in m_list:
    print(dic[i], end=' ')
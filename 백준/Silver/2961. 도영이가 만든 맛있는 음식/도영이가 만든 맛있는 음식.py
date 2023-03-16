lst = []

def backtrack(visited, k ,input):        # 요리를 부분집합으로 나타내기

    if k == input :
        res = []
        for i in range(1, input):
            if visited[i] != False:
                res.append(dish[i - 1])
        if len(res) != 0:
            lst.append(cook(res))
        return

    else:

        visited[k] = True
        backtrack(visited, k + 1, input)
        visited[k] = False
        backtrack(visited, k + 1, input)

def cook(d):                        # 입력한 요리의 신맛, 쓴맛 차이 반환
    s = 1
    b = 0

    for i in range(len(d)):
        s *= d[i][0]
        b += d[i][1]

    return abs(s - b)


N = int(input())
dish = []

for _ in range(N):
    a, b = map(int,input().split())
    dish.append((a, b))


visited = [False] * (N + 1)
backtrack(visited, 1, N + 1)

print(min(lst))
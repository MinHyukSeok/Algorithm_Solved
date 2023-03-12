N = int(input())

lst = list(map(int, input().split()))

tree = [[-1, -1, -1] for _ in range(N)]

i = 0
while lst:
    a = lst.pop(0)
    if a != -1:
        tree[i][2] = a              # 부모 지정
        if tree[a][0] == -1:        # 왼쪽 자식 없다면
            tree[a][0] = i
        else:                       # 왼쪽 자식 있다면
            tree[a][1] = i


    i += 1

remove_node = [int(input())]
r_p = tree[remove_node[0]][2]
for i in range(2):
    if tree[r_p][i] == remove_node[0]:             # 삭제할 노드의 부모 노드
        tree[r_p][i] = -1

tree[remove_node[0]][2] = -1

if N == 2 and remove_node[0] == 1:
    print(1)
else:
    while remove_node:
        r = remove_node.pop(0)

        if tree[r][0] != -1:
            remove_node.append(tree[r][0])

        if tree[r][1] != -1:
            remove_node.append(tree[r][1])

        for i in range(N):
            if tree[i][2] == r:               # 삭제할 노드의 자식 노드들
                tree[i][2] = -1

    cnt = 0
    for i in range(N):
        if tree[i][0] == -1 and tree[i][1] == -1 and tree[i][2] != -1:      # 리프 노드 찾기
            cnt += 1

    print(cnt)
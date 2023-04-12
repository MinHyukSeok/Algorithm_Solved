from collections import deque

N, M, V = map(int, input().split())
visited1 = [False] * (N + 1)
visited2 = [False] * (N + 1)
res1 = [False] * N
res2 = [False] * N
stack = []
queue = deque()

dic = {x : [] for x in range(1, N + 1)}

for i in range(M):
    a, b= map(int, input().split())
    dic[a] += [b]
    dic[b] += [a]

for i in range(1, N + 1):
    dic[i].sort()

# DFS
i = 0
stack += dic[V][::-1]
visited1[V] = True
res1[i] = V
i += 1
while stack:
    node = stack.pop()
    if visited1[node] == False:
        stack += dic[node][::-1]
        visited1[node] = True
        res1[i] = node
        i += 1

# BFS
j = 0
queue += dic[V]
visited2[V] = True
res2[j] = V
j += 1
while queue:
    node = queue.popleft()
    if visited2[node] == False:
        queue += dic[node]
        visited2[node] = True
        res2[j] = node
        j += 1

print(*res1[:i])
print(*res2[:j])
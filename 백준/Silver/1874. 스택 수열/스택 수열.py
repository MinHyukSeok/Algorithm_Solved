import sys
input = sys.stdin.readline
print = sys.stdout.write
N = int(input())
lst = []
for _ in range(N):
    lst.append(int(input()))

stack = []
idx = 1
res_idx = 0
r = ''
while res_idx < N and idx <= N + 1:
    if not stack or stack[-1] != lst[res_idx]:
        stack.append(idx)           # push
        idx += 1
        r += '+\n'

    elif stack[-1] == lst[res_idx]:
        stack.pop()
        r += '-\n'
        res_idx += 1

if stack:
    print("NO")
else:
    print(r)
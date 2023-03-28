import sys
from collections import deque
input = sys.stdin.readline
print = sys.stdout.write


N = int(input())
queue = deque()
for _ in range(N):
    t = list(input().split())
    if t[0] == 'push':
        queue.append(int(t[1]))
    elif t[0] == 'pop':
        if len(queue):
            print(f'{queue.popleft()}\n')
        else:
            print('-1\n')
    elif t[0] == 'size':
        print(f'{len(queue)}\n')
    elif t[0] == 'empty':
        if len(queue) == 0:
            print('1\n')
        else:
            print('0\n')
    elif t[0] == 'back':
        if len(queue) == 0:
            print('-1\n')
        else:
            print(f'{queue[-1]}\n')
    elif t[0] == 'front':
        if len(queue) == 0:
            print('-1\n')
        else:
            print(f'{queue[0]}\n')
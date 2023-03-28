import sys
input = sys.stdin.readline
print = sys.stdout.write


N = int(input())
stack = []
for _ in range(N):
    t = list(input().split())
    if t[0] == 'push':
        stack.append(int(t[1]))
    elif t[0] == 'pop':
        if len(stack):
            print(f'{stack.pop()}\n')
        else:
            print('-1\n')
    elif t[0] == 'size':
        print(f'{len(stack)}\n')
    elif t[0] == 'empty':
        if len(stack) == 0:
            print('1\n')
        else:
            print('0\n')
    elif t[0] == 'top':
        if len(stack) == 0:
            print('-1\n')
        else:
            print(f'{stack[-1]}\n')
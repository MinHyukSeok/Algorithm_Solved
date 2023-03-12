token = list(input())
N = len(token)
lst = []
stack = []
prior = {'*' : 3, '/' : 3, '+' : 2, '-':2, '(' : 1}

for n in range(N):
    if token[n].isalpha():
        lst.append(token[n])
    elif token[n] == '(':  # (이면 바로 stack에 추가
        stack.append(token[n])
    elif token[n] == ')':  # )가 나오면 stack에서 (가 나올때까지 pop처리 및 lst에 추가.
        while stack[-1] != '(':
            lst.append(stack.pop())
        stack.pop()  # (가 나타나면 pop처리
    else:
        while stack and prior[token[n]] <= prior[stack[-1]]:
            lst.append(stack.pop())
        stack.append(token[n])
while len(stack) != 0:
    lst.append(stack.pop())

print(''.join(lst))
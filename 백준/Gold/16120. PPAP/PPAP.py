s = input()
stack = []

for i in s:
    stack.append(i)                             # 문자열 하나씩 스택에 추가
    if len(stack) >= 4:                         # 스택의 개수가 4개 이상이라면
        if stack[-4:] == ['P', 'P', 'A', 'P']:  # PPAP인가?
            stack.pop()
            stack.pop()
            stack.pop()

if stack == ['P']:
    print('PPAP')
else:
    print('NP')
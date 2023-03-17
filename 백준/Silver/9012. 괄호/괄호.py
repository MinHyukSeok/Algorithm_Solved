t = int(input())

for test_case in range(1, t + 1):
    s = list(input())
    lst = []
    while s:
        i = s.pop(0)

        if i == '(':
            lst.append(i)
        elif i == ')':

            if len(lst) != 0 and lst[-1] == '(':
                lst.pop()
            else:
                lst.append(0)
                break

    if len(lst) == 0:
        print('YES')
    else:
        print('NO')
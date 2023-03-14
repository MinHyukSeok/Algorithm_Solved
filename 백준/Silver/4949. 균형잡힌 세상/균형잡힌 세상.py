def check(f1, f2):
    if f1 == '(' and f2 == ')':
        return True
    elif f1 == '[' and f2 == ']':
        return True
    else:
        return False


while 1:
    on_off = 1
    sentence = list(input())
    lst = []
    if len(sentence) == 1 and sentence[0] == '.':
        break
    while sentence:
        t = sentence.pop(0)
        if t == '(' or t == '[':
            lst.append(t)
        elif t == ')' or t == ']':
            if len(lst) == 0:
                on_off = 0
                break
            if check(lst[-1], t) == True:
                lst.pop()
            else:
                on_off = 0
                break
    if on_off == 1 and len(lst) == 0:
        print('yes')
    else:
        print('no')

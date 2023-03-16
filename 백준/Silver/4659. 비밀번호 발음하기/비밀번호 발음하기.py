def first_check(fs):              # 모음 검사
    if 'a' in fs:
        return True
    elif 'e' in fs:
        return True
    elif 'i' in fs:
        return True
    elif 'o' in fs:
        return True
    elif 'u' in fs:
        return True
    else:
        return False


def second_check(fs):
    if len(fs) <= 2:
        return True

    fs = list(fs)
    temp = []
    temp.append(fs.pop(0))
    temp.append(fs.pop(0))

    while fs:
        temp.append(fs.pop(0))

        if first_check(temp[0]) == True and first_check(temp[1]) == True and first_check(temp[2]) == True:
            return False
        elif first_check(temp[0]) == False and first_check(temp[1]) == False and first_check(temp[2]) == False:
            return False
        else:
            temp.pop(0)
    return True


def last_check(fs):

    fs = list(fs)
    temp = []
    temp.append(fs.pop(0))

    while fs:
        temp.append(fs.pop(0))

        if temp[0] == temp[1]:
            if temp[0] != 'e' and temp[0] != 'o':
                return False
            else:
                temp.pop(0)
        else:
            temp.pop(0)

    return True


while 1:
    s = input()
    if s == 'end':
        break
    else:
        if first_check(s) == True and second_check(s) == True and last_check(s) == True:
            print(f'<{s}> is acceptable.')
        else:
            print(f'<{s}> is not acceptable.')

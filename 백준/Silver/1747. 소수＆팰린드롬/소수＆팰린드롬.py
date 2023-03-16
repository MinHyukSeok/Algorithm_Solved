def check(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


def check2(x):
    x = str(x)

    if x == x[::-1]:
        return True
    else:
        return False


n = int(input())


while 1:
    if check2(n) == True and check(n) == True and n != 1:
        break

    else:
        n += 1


print(n)
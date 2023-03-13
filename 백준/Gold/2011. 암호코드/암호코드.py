patturn = [1, 1, 2, 3, 5, 8]
code = [str(i) for i in range(1, 27)]


def check(s):
    if s in code:
        return True
    else:
        return False

num_list = list(input())

for _ in range(len(num_list) - 3):
    patturn.append(patturn[-1] + patturn[-2])

l = 1
res = []
cnt = 1
on_off = 1

for i in range(1, len(num_list)):

    if num_list[i] == '0':
        if num_list[i - 1] + num_list[i] == '00' or int(num_list[i - 1]) > 2:
            on_off = 0
            break
        elif int(num_list[i - 1]) <= 2:
            res.append(patturn[cnt - 1])
            cnt = 1

    elif check(num_list[i - 1] + num_list[i]) == True:
        cnt += 1

    elif check(num_list[i - 1] + num_list[i]) == False:

        res.append(patturn[cnt])
        cnt = 1


if cnt != 0:
    res.append(patturn[cnt])


if num_list[0] == '0' or on_off == 0:
    print(0)

else:
    r = 1

    for i in res:
        r *= i

    print(int(r % 1000000))
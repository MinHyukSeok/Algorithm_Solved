def ten(N):                 # 2진수를 10진수로 변환
    res = 0
    N = list(N)
    i = 1
    while N:
        a = N.pop()
        if a == '1':
            res += i

        i *= 2

    return res

num1 = input()
num2 = input()

mul_num = ten(num1) * ten(num2)

mul_num = bin(mul_num)

print(mul_num[2:])
import copy

def check(down, dice):                 # 아랫면 숫자 입력받고 옆면 최댓값, 윗면 숫자 반환
    for i in range(6):
        if dice[i] == down:
            if i == 0:
                up = dice[5]
                dice[0] = dice[5] = 0
                side = max(dice)

            elif i == 1:
                up = dice[3]
                dice[1] = dice[3] = 0
                side = max(dice)
            elif i == 2:
                up = dice[4]
                dice[2] = dice[4] = 0
                side = max(dice)
            elif i == 3:
                up = dice[1]
                dice[1] = dice[3] = 0
                side = max(dice)
            elif i == 4:
                up = dice[2]
                dice[2] = dice[4] = 0
                side = max(dice)
            elif i == 5:
                up = dice[0]
                dice[0] = dice[5] = 0
                side = max(dice)

    return up, side



N = int(input())
dice_lst = []
max_num = 0

for _ in range(N):
    dice_lst.append(list(map(int, input().split())))

for i in range(0, 6):
    # d_l = dice_lst.copy()
    d_l = copy.deepcopy(dice_lst)
    res = 0
    d = d_l.pop(0)
    u ,add = check(d[i], d)
    res += add

    for j in range(N - 1):
        d = d_l.pop(0)
        u, add = check(u, d)
        res += add

    if res > max_num:
        max_num = res
print(max_num)
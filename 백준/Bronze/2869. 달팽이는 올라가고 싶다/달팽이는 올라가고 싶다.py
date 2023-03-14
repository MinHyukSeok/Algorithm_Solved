import math

a, b, v = map(int, input().split())

up_down = a - b

day = math.ceil(v / up_down)

while 1:
    if (a * day) - (b * (day - 1)) <= v:
        if (a * day) - (b * (day - 1)) < v:
            day += 1
        break

    if (a * day) - (b * (day - 1)) > v:
        day -= 1



print(day)
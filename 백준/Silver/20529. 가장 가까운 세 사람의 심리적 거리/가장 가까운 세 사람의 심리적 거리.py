mbti_type = ['ISTJ', 'ISFJ', 'INFJ', 'INTJ', 'ISTP', 'ISFP', 'INFP', 'INTP', 'ESTP', 'ESFP', 'ENFP', 'ENTP', 'ESTJ', 'ESFJ', 'ENFJ', 'ENTJ']

import sys
import itertools
# input = sys.stdin.readline
print = sys.stdout.write
# sys.setrecursionlimit(10**4)


res = []


def mbti_distance(l):
    distance = 0
    mbti_first = list(l[0])
    mbti_second = list(l[1])
    mbti_third = list(l[2])

    for i in range(4):
        if mbti_first[i] != mbti_second[i]:
            distance += 1
    for i in range(4):
        if mbti_first[i] != mbti_third[i]:
            distance += 1
    for i in range(4):
        if mbti_second[i] != mbti_third[i]:
            distance += 1

    return distance

def recur(arr, n, idx, mlist):
    global min_distance
    if idx == n:
        if len(arr) == 3:
            if min_distance > mbti_distance(arr):
                min_distance = mbti_distance(arr)
        return

    arr.append(mlist[idx])
    recur(arr, n, idx + 1, mlist)
    arr.pop()
    recur(arr, n, idx + 1, mlist)


T = int(input())

for test_case in range(T):
    min_distance = 1000000000
    res = []
    on_off = 1
    N = int(input())
    mbti_list = list(input().split(' '))
    dict = {
               'ISTJ' : 0,
               'ISFJ' : 0,
               'INFJ' : 0,
               'INTJ' : 0,
               'ISTP' : 0,
               'ISFP' : 0,
               'INFP' : 0,
               'INTP' : 0,
               'ESTP' : 0,
               'ESFP' : 0,
               'ENFP' : 0,
               'ENTP' : 0,
               'ESTJ' : 0,
               'ESFJ' : 0,
               'ENFJ' : 0,
               'ENTJ' : 0
    }

    for i in mbti_list:
        dict[i] += 1
        if dict[i] >= 3:
            on_off = 0
            min_distance = 0
            break

    if on_off == 1:
        for t in mbti_type:
            res += ([t] * dict[t])
    else:
        res.clear()

    if len(res) == 0:
        min_distance = 0
    else:
        temp = list(itertools.combinations(res, 3))

        for i in temp:
            if min_distance > mbti_distance(i):
                min_distance = mbti_distance(i)

    print(f'{str(min_distance)}\n')
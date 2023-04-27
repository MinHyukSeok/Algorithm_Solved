from collections import deque

def solution(queue1, queue2):
    cnt = 0
    length = len(queue1) + len(queue2)

    queue1 = deque(queue1)
    queue2 = deque(queue2)
    sum_q1 = sum(queue1)
    sum_q2 = sum(queue2)

    while 1:
        if cnt >= length * 2:
            return -1
        
        if sum_q1 > sum_q2:
            queue2.append(queue1.popleft())
            sum_q2 += queue2[-1]
            sum_q1 -= queue2[-1]
            cnt += 1
            
        elif sum_q1 < sum_q2:
            queue1.append(queue2.popleft())
            sum_q1 += queue1[-1]
            sum_q2 -= queue1[-1]
            cnt += 1
            
        else:
            break

    return cnt
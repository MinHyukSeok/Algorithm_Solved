from datetime import datetime

def solution(today, terms, privacies):
    answer = []
    today_y, today_m, today_d = map(int, today.split('.'))
    term_dict  = {}
    
    for i in range(len(terms)):
        type_, term = map(str, terms[i].split(' '))
        term_dict[type_] = int(term)
    
    for i in range(len(privacies)):
        current, t = map(str, privacies[i].split(' '))
        
        current_y, current_m, current_d = map(int, current.split('.'))
        
        current_m += term_dict[t]
        print(f'계산 전 현재 시간 : {current_y} {current_m} {current_d}')
        print(f'오늘 시간 : {today_y} {today_m} {today_d}')

        current_y += current_m // 12
        current_m = current_m % 12
        print(f'계산 후 현재 시간 : {current_y} {current_m} {current_d}')
        print()
        if current_m == 0:
            current_m = 12
            current_y -= 1
        
        first = datetime(current_y, current_m, current_d)
        second = datetime(today_y, today_m, today_d)
        
        if first <= second:
            answer.append(i + 1)
        
    answer.sort()
    return answer
def solution(survey, choices):
    dict_type = {'R' : 0, 'T' : 0, 'C' : 0, 'F' : 0, 'J' : 0, 'M' : 0, 'A' : 0, 'N' : 0}
    answer = ''
    
    for i in range(len(survey)):
        t = list(survey[i])
        
        if choices[i] == 1:
            dict_type[t[0]] += 3
        elif choices[i] == 2:
            dict_type[t[0]] += 2
        elif choices[i] == 3:
            dict_type[t[0]] += 1
        elif choices[i] == 5:
            dict_type[t[1]] += 1
        elif choices[i] == 6:
            dict_type[t[1]] += 2
        elif choices[i] == 7:
            dict_type[t[1]] += 3

    if dict_type['R'] < dict_type['T']:
        answer += 'T'
    else:
        answer += 'R'
    
    if dict_type['C'] < dict_type['F']:
        answer += 'F'
    else:
        answer += 'C'
        
    if dict_type['J'] < dict_type['M']:
        answer += 'M'
    else:
        answer += 'J'
        
    if dict_type['A'] < dict_type['N']:
        answer += 'N'
    else:
        answer += 'A'
    
    
    return answer
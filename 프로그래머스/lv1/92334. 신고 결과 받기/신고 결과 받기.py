def solution(id_list, report, k):
    answer = {}
    
    dict_ = {}
    
    for id in id_list:
        dict_[id] = set()
        answer[id] = 0
    
    for i in range(len(report)):
        server, receiver = map(str, report[i].split(' '))
        dict_[receiver].add(server)
    
    for id in id_list:
        if len(dict_[id]) >= k:
            for r in dict_[id]:
                answer[r] += 1
    
    res = []
    for i in range(len(id_list)):
        res.append(answer[id_list[i]])
    
    return res
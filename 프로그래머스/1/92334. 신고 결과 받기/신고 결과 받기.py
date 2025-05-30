def solution(id_list, report, k):
    reported_dict = {id: 0 for id in id_list}
    report_dict = {id: [] for id in id_list}
    #arr = [[] for _ in range(len(id_list))]
    
    for user in report:
        a,b = user.split()
        if b in report_dict[a]:
            continue
        reported_dict[b] += 1
        report_dict[a].append(b)

    
    result = [i for i, count in reported_dict.items() if count >= k]
    answer = []
    
    for key, value in report_dict.items():
        count = 0
        for k in range(len(result)):
            if result[k] in value:
                count += 1
        
        answer.append(count)
    
    return answer
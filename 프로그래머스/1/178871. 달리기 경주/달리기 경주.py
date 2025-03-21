from collections import Counter

def solution(players, callings):
    #players는 현재 등수
    #callings는 부른 이름
    
    a = {}# 등수 : 이름
    b = {} #이름 : 등수
    
    for idx, c in enumerate(players):
        a[idx+1] = c
        b[c] = idx+1
    
    for name in callings:
        cur_rank =b[name]
        next_rank = cur_rank-1
        
        a[cur_rank], a[next_rank] = a[next_rank],a[cur_rank]
        
        
        
        b[name], b[a[cur_rank]] = b[a[cur_rank]], b[name]
        
    
    answer = [i for i in a.values()]
    
    return answer
    
    
        
        
        
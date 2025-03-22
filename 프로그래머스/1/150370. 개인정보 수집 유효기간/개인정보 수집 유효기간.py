def make_to_day(year) -> int:
    a,b,c = year.split(".")
    
    
    return int(a)*12*28 + 28*int(b) + int(c) 
    
    

def solution(today, terms, privacies):
    dict_term = {}
    for term in terms:
        a,b = term.split()
        dict_term[a] = b
        
    ans = []
    
    for i in range(len(privacies)):
        day, alpha = privacies[i].split()
        day_to_day = make_to_day(day) #day_to_day가 프라이버시의 날짜
        
        print(day_to_day)
        limit = int(dict_term[alpha]) * 28
        
        today_to_day = make_to_day(today) #today_to_day가 오늘 날짜
        print(today_to_day)
        if day_to_day + limit <= today_to_day:
            ans.append(i+1)
        
    return ans
        
        
        
        
        
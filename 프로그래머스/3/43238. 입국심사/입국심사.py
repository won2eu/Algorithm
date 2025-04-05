def solution(n, times):
    #모든 사람이 심사를 받는데 걸리는 시간을 최소로 하고 싶음
    
    left, right = 1, max(times) * n
    
    answer = right
    
    while left<=right:
        mid = (left+right) // 2
        
        total = sum(mid//time for time in times)
        
        if total >=n:
            answer = mid
            right = mid-1
        else:
            left = mid+1
    
    return answer
    
        
    
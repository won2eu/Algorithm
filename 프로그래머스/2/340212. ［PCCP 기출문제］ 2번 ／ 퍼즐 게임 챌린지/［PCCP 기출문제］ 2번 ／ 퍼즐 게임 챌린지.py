def solution(diffs, times, limit):
    '''
    n개의 퍼즐을 푸는데
    각 퍼즐은 난이도 / 소요시간
    나의 숙련도로 틀리는 횟수가 정해짐
    '''
    
    #diff <= level이면 틀리지않고 time_cur로 해결
    #diff > level이면 diff-level만큼 틀림
    
    #틀릴때마다 time_cur만큼 사용
    #time_prev만큼 다시 풀어야함 단 다시 풀땐 틀리지않고 time_cur만에 바로 품
    
    #숙련도의 최소값이니까 level을 1부터 시작해서 하나씩 올려가보면서 limit을 넘으면 바로 break
    level = 1
    time_prev = 0
    left, right = 1, max(diffs)

    while left<right:
        level = (left + right) // 2
        can_do_it = False
        now = 0
        time_prev = 0
        for i in range(len(diffs)):
            

            if diffs[i] <= level:
                now += times[i]
            else:
                now += (times[i]+time_prev)*(diffs[i]-level) + times[i] 

            if now > limit:
                break
                
            # if (i==len(diffs)-1):
            #     can_do_it = True
                
            time_prev = times[i]
            
#         if can_do_it:
#             return level
        
#         else:
#             level += 1
        if now <= limit:  # 가능하면 바로 반환
            right = level
        else:
            left = level + 1  # 더 높은 level 필요
        

                
    return left
                
        
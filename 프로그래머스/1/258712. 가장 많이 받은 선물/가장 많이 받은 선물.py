def solution(friends, gifts):
    #1. 선물지수 기록하기
    
    #2. 준 사람 / 받은 사람 기록하는 2차원 배열 만들기
    n = len(friends)
    friend_index = {friends[i]: i for i in range(n)}
    gift_count = {name : [0,0] for name in friends}
    
    gift_matrix = [[0]*n for _ in range(n)]
    
    for record in gifts:
        giver, receiver = record.split()
        giver_idx = friend_index[giver]
        receiver_idx = friend_index[receiver]
        
        gift_count[giver][0] += 1
        gift_count[receiver][1] += 1
        gift_matrix[giver_idx][receiver_idx] += 1
    
    receive_next = [0] * n
    
    for i in range(n):
        for j in range(n):
            if i==j:
                continue
            
            if gift_matrix[i][j] > gift_matrix[j][i]:
                receive_next[i] += 1
            elif gift_matrix[i][j] == gift_matrix[j][i]:
                
                sunmul_i = gift_count[friends[i]][0] - gift_count[friends[i]][1]
                sunmul_j = gift_count[friends[j]][0] - gift_count[friends[j]][1]
                
                if sunmul_i > sunmul_j :
                    receive_next[i] += 1
                
    return max(receive_next)
        
        
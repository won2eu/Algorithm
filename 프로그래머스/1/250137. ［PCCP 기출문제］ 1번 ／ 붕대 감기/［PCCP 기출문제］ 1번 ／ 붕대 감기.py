def solution(bandage, health, attacks):
    max_health = health
    time_for_heal = 0
    time = 0
    while time <= attacks[-1][0]:
        attack_flag = False
        for i in attacks: 
            if i[0] == time:#시간이 0초부터 흘러서 attacks에 해당하는 공격 시간 이라면
                health -= i[1] #데미지를 입히고
                time_for_heal = 0 #시전시간 초기화
                attack_flag = True #공격당함 표시
                
                if health <= 0:
                    return -1
        if not attack_flag:
            time_for_heal += 1
            
        if not attack_flag: #해당 time이 공격시간이 아니라면
            if health != max_health: #체력이 풀피가 아니라면
                health += bandage[1] #체력을 더하고
                if health > max_health: #체력이 최대체력보다 많다면
                    health = max_health #최대체력으로 바꿔주기

            if time_for_heal == bandage[0]: #시전시간만큼 연속으로 힐했다면
                health += bandage[2] # 체력회복
                time_for_heal = 0
                if health > max_health: #최대체력보다 많다면
                    health = max_health #최대체력으로
        

        
        time += 1 #기존시간 1초 더 흐름

    return health
        
        
        
        
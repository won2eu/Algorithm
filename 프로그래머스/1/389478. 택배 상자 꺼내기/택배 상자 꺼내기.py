def solution(n, w, num): #n: 상자 갯수 w: 가로로 놓는 수 num: 꺼내려는 상자 번호
    arr = [[0] * (w) for _ in range(n//w+1)]
    value = 1
    found = False
    
    for i in range(n//w+1):
        if (i%2 == 0):
            for j in range(w):
                arr[i][j] = value
                
                if value == n:
                    found = True
                    break
                value += 1
        
        else:
            for j in range(w-1,-1,-1):
                arr[i][j] = value
                
                if value == n:
                    found = True
                    break
                
                value += 1
        if found:
            break
                
    for i in range(len(arr)):
        for j in range(w):
            if arr[i][j] == num:
                row = j
                column = i
                break
    cnt = 0
    
    for i in range(column, len(arr)):
        if (arr[i][row] !=0):
            cnt += 1
    print(arr)
    return cnt
    
            
            
            
    
    
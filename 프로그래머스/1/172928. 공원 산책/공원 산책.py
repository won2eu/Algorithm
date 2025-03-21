def solution(park, routes):
    height = len(park)
    width = len(park[0])
    
    def in_range(x,y):
        return 0<=x<height and 0<=y<width
    
    arr = [[0] * width for _ in range(height)]
    
    for i in range(height):
        for j in range(width):
            arr[i][j] = park[i][j]
            if arr[i][j] == "S":
                x, y = i, j
    
    
    for route in routes:
        a,b = route.split()
        n = int(b)
        flag = False
        print(a,b)
        if a=="N": #뒤로감
            if in_range(x-n,y):
                for i in range(x-n, x):
                    if arr[i][y] == 'X':
                        flag=True
                        break
                if flag == True:
                    continue
                x = x-n
        
        if a=="S":
            if in_range(x+n,y):
                for i in range(x+1, x+n+1):
                    if arr[i][y] == 'X':
                        flag = True
                        break
                if flag == True:
                    continue
                x = x+n
        
        if a=="W": #뒤로감
            if in_range(x,y-n):
                for i in range(y-n, y):
                    if arr[x][i] == 'X':
                        flag = True
                        break
                if flag == True:
                    continue
                y = y-n
        
        if a=="E": 
            if in_range(x,y+n):
                for i in range(y+1, y+n+1):
                    if arr[x][i] == 'X':
                        flag = True
                        break
                if flag == True:
                    continue
                y= y+n
        print(x,y)
    return [x,y]
    
    
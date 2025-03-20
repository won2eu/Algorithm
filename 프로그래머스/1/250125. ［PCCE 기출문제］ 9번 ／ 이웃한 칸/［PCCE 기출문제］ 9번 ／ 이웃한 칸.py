def solution(board, h, w):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1 ,1]
    
    row = len(board)
    col = len(board[0])
    
    count = 0
    
    def in_range(x,y):
        return x>=0 and y>=0 and x< col and y<row
        
    
    for i in range(4):
        nx = h + dx[i]
        ny = w + dy[i]
        
        if in_range(nx,ny):
            if board[nx][ny] == board[h][w]:
                count += 1
                
    return count
            
        
    
    
    
    
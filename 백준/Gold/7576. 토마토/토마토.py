from collections import deque #큐 사용하기 위해 deque import

m,n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]  #입력받기

visited = [[False] * m for _ in range(n)] #방명록
result = []
dx = [0,0,-1,1]
dy = [1,-1,0,0]


def bfs(): #출발점 x,y에서 bfs 탐색하는 알고리즘
    queue = deque()
    day = -1 #마지막에 큐가 비었을때도 1증가시키기 때문에 -1로 설정
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                queue.append([i,j])

    while queue:
        for _ in range(len(queue)):
            x,y = queue.popleft()
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < n and 0 <= ny < m:
                    if visited[nx][ny] == False and arr[nx][ny] == 0:
                        arr[nx][ny] = 1
                        visited[nx][ny] = True
                        queue.append([nx,ny])
                        
        day += 1

    
    for x in arr:
        if 0 in x:
            return -1
    
    return day


print(bfs())

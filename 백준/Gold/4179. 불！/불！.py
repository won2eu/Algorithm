from collections import deque #큐 사용하기 위해 deque import

n,m = map(int, input().split())
arr = [list(map(str, input().strip())) for _ in range(n)]  #입력받기

J_visited = [[False] * m for _ in range(n)] #지훈이 방명록
F_visited = [[False] * m for _ in range(n)] #불 방명록

F_time = [[float('inf')]*m for _ in range(n)]
J_time = [[0]*m for _ in range(n)]

result = []
dx = [0,0,-1,1]
dy = [1,-1,0,0]


def bfs(): #출발점 x,y에서 bfs 탐색하는 알고리즘
    J_queue = deque()
    F_queue = deque()
    
    for i in range(n):
            for j in range(m):
                if arr[i][j] == "F":
                    F_queue.append([i,j])
                    F_visited[i][j] = True
                    F_time[i][j] = 0

                if arr[i][j] == "J":
                    J_queue.append([i,j])
                    J_visited[i][j] = True




    while F_queue:
        x,y = F_queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if F_visited[nx][ny] == False and arr[nx][ny] == ".":
                    F_time[nx][ny] = F_time[x][y] + 1
                    F_visited[nx][ny] = True
                    F_queue.append([nx,ny])

    while J_queue:
        x,y = J_queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m:
                if J_visited[nx][ny] == False and arr[nx][ny] == "." and J_time[x][y] + 1 < F_time[nx][ny]:
                    J_time[nx][ny] = J_time[x][y] + 1
                    J_visited[nx][ny] = True
                    J_queue.append([nx,ny])

    for i in range(n):
        for j in range(m):
            if arr[i][j] != "#" and J_visited[i][j] and J_time[i][j] < F_time[i][j]:
                arr[i][j] = "J"
            elif arr[i][j] != "#" and F_visited[i][j] and J_time[i][j] >= F_time[i][j]:
                arr[i][j] = "F"


    escape_time = float('inf')
    for i in range(n):
        for j in range(m):
            if arr[i][j] == "J":
                if i==0 or i==n-1 or j==0 or j==m-1:
                    escape_time = min(escape_time,J_time[i][j]+1)
    
    if escape_time == float('inf'):
        return "IMPOSSIBLE"

    else:
        return escape_time

ec_time = bfs()
print(ec_time)


from collections import deque #큐 사용하기 위해 deque import

n,m = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(n)]  #입력받기

visited = [[False] * m for _ in range(n)] #방명록
result = []
dx = [0,0,-1,1]
dy = [1,-1,0,0]

def bfs(x,y): #출발점 x,y에서 bfs 탐색하는 알고리즘
    queue = deque()
    queue.append([x,y])

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == False and arr[nx][ny] == 1:
                    arr[nx][ny] = arr[x][y] + 1
                    visited[nx][ny] = True
                    queue.append([nx,ny])

bfs(0,0)
print(arr[n-1][m-1])

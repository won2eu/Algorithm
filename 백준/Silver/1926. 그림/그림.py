from collections import deque

n, m = map(int, input().split())
visited = [[False] * m for _ in range(n)] #방명록

graph = [list(map(int, input().split())) for _ in range(n)] #그래프
result = []
dx = [0,0,-1,1]
dy = [1,-1,0,0]

def bfs(x,y):
    queue = deque()
    queue.append([x,y])
    count = 1

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == False and graph[nx][ny] == 1:
                    visited[nx][ny] = True
                    count += 1
                    queue.append([nx,ny])
    return count

for x in range(n):
    for y in range(m):
        if visited[x][y] == False and graph[x][y] == 1:
            visited[x][y] = True
            ans = bfs(x,y)
            result.append(ans)
            
if len(result) == 0:
    print(0)
    print(0)

else:
    print(len(result))
    print(max(result))
from collections import deque

T = int(input())

dx = [-1,1,0,0]
dy = [0,0,1,-1]


def bfs(x,y):
    queue = deque()
    queue.append([x,y])
    visited[y][x] = True
    
    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < m and 0 <= ny < n and baechu[ny][nx] and visited[ny][nx] == False:
                visited[ny][nx] = True
                queue.append([nx,ny])

for _ in range(T):
    m,n,k = map(int, input().split())
    cnt = 0
    visited = [[False] * m for _ in range(n)]
    baechu = [[0] * m for _ in range(n)]

    for _ in range(k):
            x,y = map(int, input().split())
            baechu[y][x] = 1

    for y in range(n):
        for x in range(m):
            if baechu[y][x] and not visited[y][x]:
                bfs(x,y)
                cnt += 1

    print(cnt)
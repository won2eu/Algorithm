from collections import deque

n,m = map(int, input().split())
arr = [0]*100001
visited = [False] *100001

def bfs():
    queue = deque()
    queue.append(n)
    visited[n] = True
    
    while queue:
        x = queue.popleft()

        if x == m:
            return(arr[x])

        for nx in (x-1, x+1, x*2):
            if 0<=nx<=100000 and visited[nx] == False:
                visited[nx] = True
                arr[nx] = arr[x] + 1
                queue.append(nx)


ans = bfs()
print(ans)
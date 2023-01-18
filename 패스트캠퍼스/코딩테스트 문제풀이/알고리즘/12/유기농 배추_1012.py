import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

def bfs (graph, visit, s_y, s_x, m, n):
    queue = deque([(s_y,s_x)])
    visit[s_y][s_x] = True
    graph[s_y][s_x] = 0
    while queue:
        y,x = queue.popleft()
        for (dy,dx) in [(-1,0), (0,1), (1,0), (0,-1)]:
            ny, nx = dy+y, dx+x
            if ny >= 0 and nx >= 0 and ny < n and nx < m and not visit[ny][nx] and graph[ny][nx]:
                queue.append((ny,nx))
                graph[ny][nx] = 0
                visit[ny][nx] = True

for _ in range(T):
    m, n, k = map(int, input().split())
    graph = [[0] * m for __ in range(n)]
    visit = [[False] * m for __ in range(n)]
    answer = 0
    
    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1
        
    for i in range(n):
        for j in range(m):
            if graph[i][j]:
                bfs(graph, visit, i, j, m, n)
                answer += 1
                
    
    print(answer)
    




import sys
from collections import deque
input = sys.stdin.readline

M, N = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))
visit = [[False] * M for _ in range(N)]

def get_tomatoes():
    tomatoes = []
    for i in range(N):
        for j in range(M):
            if board[i][j] == 1:
                tomatoes.append((i,j))
    return tomatoes

def bfs():
    queue = deque([])
    tomatoes = get_tomatoes()
    max_dist = 0
    for y,x in tomatoes:
        queue.append((y,x,0))
        visit[y][x] = True
    
    while queue:
        y, x, dist = queue.popleft()
        max_dist = max(max_dist, dist)
        for dy, dx in [(-1,0), (0,1), (1,0), (0,-1)]:
            ny, nx = dy + y, dx + x
            if ny < 0 or nx < 0 or ny >= N or nx >= M: continue
            if visit[ny][nx]: continue
            if board[ny][nx] == -1: continue
            visit[ny][nx] = True
            board[ny][nx] = 1
            queue.append((ny,nx,dist+1))
    
    return max_dist   

max_dist = bfs()
for i in range(N):
    for j in range(M):
        if board[i][j] == 0: 
            print(-1)
            exit(0)
print(max_dist)
        
        
    
    
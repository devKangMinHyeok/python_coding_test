import sys
from collections import deque
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

N = int(input())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))
visit = [[False] * N for _ in range(N)]
distances = [[float("inf")] * N for _ in range(N)]
label = 1

def dfs(y,x, label):
    visit[y][x] = True
    board[y][x] = label
    for dy, dx in [(-1,0), (0,1), (1,0), (0,-1)]:
        ny, nx = dy + y, dx + x
        if ny < 0 or nx < 0 or ny >= N or nx >= N: continue
        if visit[ny][nx]: continue
        if board[ny][nx] == 0: continue
        visit[ny][nx] = True
        dfs(ny,nx, label)

def bfs(i,j, label):
    queue = deque([])
    visit = [[False] * N for _ in range(N)]
    queue.append((i,j,0))
    visit[i][j] = True
    
    while queue:
        y, x, dist = queue.popleft()
        if board[y][x] != 0 and board[y][x] != label: 
            distances[y][x] = dist
            return
        for dy, dx in [(-1,0), (0,1), (1,0), (0,-1)]:
            ny, nx = dy + y, dx + x
            if ny < 0 or nx < 0 or ny >= N or nx >= N: continue
            if visit[ny][nx]: continue
            if board[ny][nx] == label: continue
            visit[ny][nx] = True
            queue.append((ny,nx,dist+1))
    

for i in range(N):
    for j in range(N):
        if board[i][j] == 1 and not visit[i][j]:
            dfs(i,j,label)
            label += 1
    
for i in range(N):
    for j in range(N):
        if board[i][j] != 0:
            bfs(i,j,board[i][j])

min_dist = float("inf")

for d in distances:
    for dist in d:
        min_dist = min(min_dist, dist)

print(min_dist - 1)
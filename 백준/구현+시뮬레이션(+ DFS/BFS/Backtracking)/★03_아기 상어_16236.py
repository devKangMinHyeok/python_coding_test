import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
board = []
shark_size = 2
for _ in range(N):
    board.append(list(map(int, input().split())))

def find_shark():
    for i in range(N):
        for j in range(N):
            if board[i][j] == 9: return (i, j)

def find_minimum_dist(s_y, s_x):
    queue = deque([(s_y, s_x, 0)])
    visit = [[False] * N for _ in range(N)]
    visit[s_y][s_x] = True
    targets = []
    
    while queue:
        y, x, dist = queue.popleft()  
        for dy, dx in [(-1,0), (0,-1), (1,0), (0,1)]:
            ny, nx = dy + y, dx + x
            if ny < 0 or nx < 0 or ny >= N or nx >= N: continue
            if visit[ny][nx]: continue
            if board[ny][nx] > shark_size: continue
            elif board[ny][nx] == 0 or board[ny][nx] == shark_size:
                queue.append((ny, nx, dist+1))
            elif board[ny][nx] < shark_size: 
                targets.append((dist+1, ny, nx))
            visit[ny][nx] = True
    if not targets: return (-1,-1,0)
    else:
        targets.sort(key = lambda x : (x[0], x[1], x[2]))
        return targets[0]

y,x = find_shark()
eats = 0
answer = 0

while True:
    board[y][x] = 0
    dist, new_y, new_x = find_minimum_dist(y, x)
    if dist == -1: break
    eats += 1
    if eats == shark_size:
        shark_size += 1
        eats = 0
    answer += dist
    y, x = new_y, new_x

print(answer)
    
        
    
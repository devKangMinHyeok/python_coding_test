import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
board = []

for _ in range(N):
    row = list(map(int, input().split()))
    board.append(row)

count = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == 1: count += 1

def find_air():
    queue = deque([(0,0)])
    air = [[False] * M for _ in range(N)]
    air[0][0] = True
    
    while queue:
        y, x = queue.popleft()
        for dy, dx in [(1,0),(0,1),(-1,0),(0,-1)]:
            ny, nx = dy + y, dx + x
            if ny < 0 or nx < 0 or ny >= N or nx >= M: continue
            if air[ny][nx]: continue
            if board[ny][nx]: continue
            air[ny][nx] = True
            queue.append((ny,nx))
    return air

def check (y, x):
    cnt = 0
    for dy, dx in [(1,0),(0,1),(-1,0),(0,-1)]:
        ny, nx = dy + y, dx + x
        if ny < 0 or nx < 0 or ny >= N or nx >= M: continue
        if air[ny][nx]:
            cnt += 1
    if cnt >= 2:
        return True
    else:
        return False
    

def get_next_board():
    global count
    for i in range(N):
        for j in range(M):
            if board[i][j] == 1:
                if check(i,j): 
                    board[i][j] = 0
                    count -= 1

answer = 0

while count:
    air = find_air()
    get_next_board()
    answer += 1

print(answer)
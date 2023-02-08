import sys
from collections import deque
input = sys.stdin.readline

def bfs(y,x):
    cnt = 1
    visit[y][x] = True
    queue = deque([(y,x)])
    
    while queue:
        y_, x_ = queue.popleft()
        for dy, dx in [(1,0), (0,1), (-1,0), (0,-1)]:
            ny, nx = dy + y_, dx + x_
            if ny < 0 or nx < 0 or ny >= N or nx >= N: continue
            if visit[ny][nx]: continue
            if board[ny][nx] == "0": continue
            visit[ny][nx] = True
            queue.append((ny,nx))
            cnt += 1
    return cnt
            

N = int(input())
board = []
visit = [[False] * N for _ in range(N)]
for _ in range(N):
    board.append(list(input()))

answer = []

for i in range(N):
    for j in range(N):
        if not visit[i][j] and board[i][j] == "1":
            ans = bfs(i,j)
            if ans: answer.append(ans)
answer.sort()
print(len(answer))
for i in answer:
    print(i)
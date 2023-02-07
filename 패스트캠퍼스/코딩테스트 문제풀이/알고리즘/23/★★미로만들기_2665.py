from heapq import heappush, heappop

n = int(input())
board = []
visit = [[0] * n for _ in range(n)]

for _ in range(n):
    board.append(list(input()))

for i in range(n):
    for j in range(n):
        board[i][j] = int(board[i][j])

queue = []
heappush(queue, (1,0,0))
visit[0][0] = 1

while queue:
    cnt, y, x = heappop(queue)
    for dy, dx in [(1,0), (0,1), (-1,0),(0,-1)]:
        ny, nx = dy + y, dx + x
        if ny < 0 or nx < 0 or ny >= n or nx >= n: continue
        if visit[ny][nx]: continue
        if board[ny][nx] == 0:
            visit[ny][nx] = cnt + 1
            heappush(queue, (cnt+1, ny, nx))
        else:
            visit[ny][nx] = cnt
            heappush(queue, (cnt, ny, nx))

print(visit[n-1][n-1]-1)
            

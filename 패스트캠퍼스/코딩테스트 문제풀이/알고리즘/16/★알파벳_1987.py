row, col = map(int, input().split())
board = []

for _ in range(row):
    board.append(input())
    
visit = [False] * (ord('Z')+1)
max_len = 0

def dfs(y,x,cnt):
    global max_len
    max_len = max(max_len, cnt)
    for dy, dx in [(1,0), (0,1), (-1,0), (0,-1)]:
        ny, nx = dy + y, dx + x
        if ny < 0 or nx < 0 or ny >= row or nx >= col: continue
        if visit[ord(board[ny][nx])]: continue
        visit[ord(board[ny][nx])] = True
        dfs(ny,nx,cnt+1)
        visit[ord(board[ny][nx])] = False

visit[ord(board[0][0])] = True
dfs(0,0,1)
print(max_len)

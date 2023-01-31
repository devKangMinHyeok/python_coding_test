r, c = map(int, input().split())
board = []
for _ in range(r):
    board.append(list(input()))

path = [False] * (ord('Z')+1)

path[ord(board[0][0])] = True
max_val = 1

def dfs(y,x,cnt):
    global max_val
    flag = False
    for dy, dx in [(0,-1), (1,0), (0,1), (-1,0)]:
        ny, nx = dy + y, dx + x
        if ny < 0 or nx < 0 or ny >= r or nx >= c: continue
        if path[ord(board[ny][nx])] : continue
        flag = True
        path[ord(board[ny][nx])] = True
        dfs(ny,nx,cnt+1)
        path[ord(board[ny][nx])] = False
    if not flag:
        max_val = max(cnt, max_val)
dfs(0,0,1)
print(max_val)
        
    
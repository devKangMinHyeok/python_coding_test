import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def dfs(y,x):
    visit[y][x] = True
    for dy, dx in [(1,0), (0,1), (-1,0), (0,-1)]:
        ny, nx = dy + y, dx + x
        if ny < 0 or nx < 0 or ny >= N or nx >= M: continue
        if visit[ny][nx]: continue
        if board[ny][nx] == 0: continue
        dfs(ny,nx)

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    board = [[0] * M for _ in range(N)]
    visit = [[False] * M for _ in range(N)]
    cnt = 0
    
    for __ in range(K):
        x, y = map(int, input().split())
        board[y][x] = 1
        
    for i in range(N):
        for j in range(M):
            if board[i][j] == 1 and not visit[i][j]: 
                dfs(i,j)
                cnt += 1
    print(cnt)
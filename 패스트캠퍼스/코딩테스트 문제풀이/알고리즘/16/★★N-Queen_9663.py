N = int(input())

board = [-1] * N
ans = 0

def can(y,x):
    for i in range(y):
        if board[i] == x:
            return False
        if abs(y-i) == abs(x-board[i]):
            return False
    return True

def dfs(y):
    global ans
    if y == N:
        ans += 1
        return
    for i in range(N):
        if can(y, i):
            board[y] = i
            dfs(y+1)
            board[y] = -1

dfs(0)
print(ans)
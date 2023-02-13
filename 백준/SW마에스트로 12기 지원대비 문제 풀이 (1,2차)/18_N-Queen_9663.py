N = int(input())
answer = 0
board = [-1] * N 

def can_set(y, x):
    if y == 0: return True
    for i in range(y):
        if board[i] == x: return False
        if abs(board[i]-x) == abs(y - i): return False
    return True

def dfs(x):
    global answer
    if x == N:
        answer += 1
        return
    for i in range(N):
        if can_set(x, i):
            board[x] = i
            dfs(x+1)
            board[x] = -1

dfs(0)
print(answer)
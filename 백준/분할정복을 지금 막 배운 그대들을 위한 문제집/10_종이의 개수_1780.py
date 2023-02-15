import sys
input = sys.stdin.readline

N = int(input())
board = []
cnt_table = {-1: 0, 0: 0, 1: 0}
for _ in range(N):
    board.append(list(map(int, input().split())))

def check_num(sy, ey, sx, ex, num):
    for i in range(sy, ey+1):
        for j in range(sx, ex+1):
            if board[i][j] != num: return False
    return True

def solve(sy, ey, sx, ex):
    length = ey - sy + 1
    if length == 1:
        target = board[sy][sx]
        cnt_table[target] += 1
    else:
        for i in [-1,0,1]:
            if check_num(sy, ey, sx, ex, i):
                cnt_table[i] += 1
                return
        offset = length // 3
        for ny in range(sy, ey+1, offset):
            for nx in range(sx, ex+1, offset):
                solve(ny, ny+offset-1, nx, nx+offset-1)
        

solve(0,N-1,0,N-1)
for i in [-1, 0, 1]:
    print(cnt_table[i])
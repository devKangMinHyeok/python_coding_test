import sys
input = sys.stdin.readline
N = int(input())
board = []
blue = 0
white = 0

for _ in range(N):
    board.append(list(map(int, input().split())))

def check_blue(sy, sx, ey, ex):
    for i in range(sy, ey+1):
        for j in range(sx, ex+1):
            if board[i][j] == 0: return False
    return True

def check_white(sy, sx, ey, ex):
    for i in range(sy, ey+1):
        for j in range(sx, ex+1):
            if board[i][j] == 1: return False
    return True

def solve(sy, sx, ey, ex):
    global blue, white
    length = ey-sy+1
    if length == 1:
        if board[sy][sx] == 1:
            blue += 1
        else:
            white += 1
        return
    else:
        if check_blue(sy, sx, ey, ex):
            blue += 1
        elif check_white(sy, sx, ey, ex):
            white += 1
        else:
            offset = length // 2
            solve(sy,sx,ey-offset,ex-offset)
            solve(sy,sx+offset,ey-offset,ex)
            solve(sy+offset,sx,ey,ex-offset)
            solve(sy+offset,sx+offset,ey,ex)

solve(0,0,N-1,N-1)
print(white)
print(blue)
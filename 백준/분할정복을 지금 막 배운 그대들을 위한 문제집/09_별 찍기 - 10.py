N = int(input())

board = [[False] * N for _ in range(N)]

def solve(sy,sx,ey,ex):
    length = ey-sy+1
    if length == 3:
        for i in range(sy, ey+1):
            for j in range(sx, ex+1):
                if i == sy+1 and j == sx+1: continue
                board[i][j] = True
    else:
        offset = length // 3
        for ny in range(sy,ey+1,offset):
            for nx in range(sx, ex+1,offset):
                if ny == sy + offset and nx == sx + offset: continue
                solve(ny,nx,ny+offset-1, nx+offset-1)

solve(0,0,N-1,N-1)
for b in board:
    for i in b:
        if i: print("*", end="")
        else: print(" ", end="")
    print("")
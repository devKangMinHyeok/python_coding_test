import sys
K = int(input())
N = pow(2,K)
tx, ty = map(int, input().split())
tx -= 1
ty -= 1
if tx < 0 or ty < 0 or tx >= N or ty >= N: 
    print(-1)
    exit(0)
board = [[0]* N for _ in range(N)]
board[ty][tx] = -1
cnt = 1

def solve(x, y, length, tag, special):
    global cnt
    if length == 2 and (tx,ty) in [(x,y), (x+1,y), (x,y+1), (x+1,y+1)]:
        for nx, ny in [(x,y), (x+1,y), (x,y+1), (x+1,y+1)]:
            if ty == ny and tx == nx: continue
            board[ny][nx] = cnt
        cnt += 1
    elif length == 2:
        if tag == "rightup":
            for nx, ny in [(x,y), (x+1,y), (x,y+1), (x+1,y+1)]:
                if ny == y+1 and nx == x: board[ny][nx] = special
                else: board[ny][nx] = cnt
            cnt += 1
        elif tag == "rightdown":
            for nx, ny in [(x,y), (x+1,y), (x,y+1), (x+1,y+1)]:
                if ny == y and nx == x: board[ny][nx] = special
                else: board[ny][nx] = cnt
            cnt += 1
        elif tag == "leftup":
            for nx, ny in [(x,y), (x+1,y), (x,y+1), (x+1,y+1)]:
                if ny == y+1 and nx == x+1: board[ny][nx] = special
                else: board[ny][nx] = cnt
            cnt += 1
        elif tag == "leftdown":
            for nx, ny in [(x,y), (x+1,y), (x,y+1), (x+1,y+1)]:
                if ny == y and nx == x+1: board[ny][nx] = special
                else: board[ny][nx] = cnt
            cnt += 1
    else:
        offset = length//2
        new_special = cnt + 0
        cnt += 1
        solve(x,y, offset, "leftup", new_special)
        solve(x+offset,y,offset, "rightup",new_special)
        solve(x,y+offset,offset, "leftdown", new_special)
        solve(x+offset,y+offset,offset, "rightdown", new_special)
        
        
    
solve(0,0,N, "", -1)
for i in range(len(board)-1, -1, -1):
    print(" ".join(map(str, board[i])))
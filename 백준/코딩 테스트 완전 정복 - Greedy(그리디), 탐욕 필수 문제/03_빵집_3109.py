import sys
input = sys.stdin.readline

R, C = map(int, input().split())
visit = [[False] * C for _ in range(R)]
board = [list(input().strip()) for _ in range(R)]

def can_go(y,x):
    if visit[y][x] or board[y][x] == "x": return False
    else: return True

def find_route(y,x):
    global answer
    visit[y][x] = True
    if x == C-1:
        answer += 1 
        return True
    for dy, dx in [(-1, 1), (0, 1), (1, 1)]:
        ny, nx = dy + y, dx + x
        if ny < 0 or nx < 0 or ny >= R or nx >= C: continue
        if not can_go(ny,nx): continue
        visit[ny][nx] = True
        if find_route(ny,nx):
            return True
    return False
    
answer = 0
for y in range(R):
    find_route(y, 0)
      
print(answer)

"""
------------------------

import sys
input = sys.stdin.readline

R, C = map(int, input().split())
answer = 0
visit = [[False] * C for _ in range(R)]
board = [list(input().strip()) for _ in range(R)]

def can_go(y,x):
    if visit[y][x] or board[y][x] == "x": return False
    else: return True

def find_route(y,x):
    global answer
    if x == C-1:
        return True
    for dy, dx in [(-1, 1), (0, 1), (1, 1)]:
        ny, nx = dy + y, dx + x
        if ny < 0 or nx < 0 or ny >= R or nx >= C: continue
        if not can_go(ny,nx): continue
        visit[ny][nx] = True
        if find_route(ny,nx):
            return True
    return False

    
for y in range(R):
    if find_route(y, 0): answer += 1
      
print(answer)
"""
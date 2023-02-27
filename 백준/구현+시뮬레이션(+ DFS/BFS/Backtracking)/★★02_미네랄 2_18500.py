import sys
sys.setrecursionlimit(100000)
R, C = map(int, input().split())
board = []
for _ in range(R):
    board.append(list(input()))
board = list(reversed(board))
N = int(input())
throws = list(map(int, sys.stdin.readline().split()))

def destroy(level, direction):
    start = 0
    end = C
    if direction == -1: # 왼쪽 <- 오른쪽
        start = C-1
        end = -1
    for i in range(start, end, direction):
        if board[level][i] == "x": 
            board[level][i] = "."
            return (level, i)
    return (-1,-1)

def find_sets(y,x,visit):
    for dy, dx in [(-1,0), (0,1), (1,0), (0,-1)]:
        ny, nx = dy + y, dx + x
        if ny < 0 or nx < 0 or ny >= R or nx >= C: continue
        if board[ny][nx] == ".": continue
        if (ny, nx) in visit: continue
        else:
            visit.add((ny,nx))
            find_sets(ny,nx,visit)
    return True
    
def is_root(visit):
    for y,x in visit:
        if y == 0: return True
    return False

def get_down(visit):
    while True:
        new_visit = set()
        for y,x in visit:
            new_visit.add((y-1,x))
        for y,x in new_visit:
            if y == -1: 
                return True
            if board[y][x] == "x" and (y,x) not in visit: 
                return True
        for y,x in visit:
            board[y][x] = "."
        for y,x in new_visit:
            board[y][x] = "x"
        visit = new_visit

def print_board():
    for b in list(reversed(board)):
        print("".join(b))  

# completed = set()
# for i in range(R):
#     for j in range(C):
#         if (i,j) in completed: continue
#         if board[i][j] == "x":
#             visit = set()
#             find_sets(i,j,visit)
#             if not is_root(visit):
#                 get_down(visit)
#                 for y,x in visit:
#                     completed.add((y,x))

for i, level in enumerate(throws):
    direction = 1
    if i % 2 != 0: direction = -1
    y, x = destroy(level-1, direction)
    if y == -1: continue
    for dy, dx in [(-1,0),(0,1), (1,0), (0,-1)]:
        ny, nx = dy + y, dx + x
        if ny < 0 or nx < 0 or ny >= R or nx >= C: continue
        if board[ny][nx] == ".": continue
        visit = set()
        visit.add((ny,nx))
        find_sets(ny,nx,visit)
        if is_root(visit): continue
        else: 
            get_down(visit)
print_board()
        


    
                
            

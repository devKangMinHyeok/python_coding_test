import sys
from collections import deque
input = sys.stdin.readline

def find_cross(index):
    y = index // 3
    x = index % 3
    return (y,x)

def get_index(y,x):
    index = 0
    index += y * 3
    index += x
    return index

def make_next(state):
    result = []
    i = state.index("9")
    y,x = find_cross(i)
    
    for dy, dx in [(-1,0), (0,1), (1,0), (0,-1)]:
        ny, nx = dy + y, dx + x
        if ny < 0 or nx < 0 or ny >= 3 or nx >= 3: continue
        new_i = get_index(ny, nx)
        new_state = list(state)
        new_state[new_i], new_state[i] = new_state[i], new_state[new_i]
        result.append("".join(new_state))
    return result

board = []
for _ in range(3):
    board.append(list(map(int, input().split())))

target = []

for i in range(3):
    for j in range(3):
        temp = board[i][j]
        if temp == 0: 
            temp = 9
        target.append(temp)
        

cur = "".join(map(str, target))
target = "".join(map(str, sorted(target)))

visit = set()
queue = deque([])
queue.append((cur, 0))
visit.add(cur)

while queue:
    prev, dist = queue.popleft()
    if prev == target: 
        print(dist)
        exit(0)
    result = make_next(prev)
    
    for next_ in result:
        if next_ in visit: continue
        else:
            queue.append((next_, dist+1))
            visit.add(next_)

print(-1)
            

    

        
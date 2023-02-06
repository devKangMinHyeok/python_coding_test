from collections import deque

a, b, c, d = map(int, input().split())

queue = deque([(0,0,0)])
visit = set()
visit.add((0,0))

find = False
answer = []

while queue:
    x, y, level = queue.popleft()
    if x == c and y == d:
        answer.append(level)
        find = True
        break
    next_state = [(a,y), (x,b), (0,y), (x,0)]
    if x <= b-y:
        next_state.append((0,x+y))
    else:
        next_state.append((x-(b-y),b))
    
    if y <= a-x:
        next_state.append((x+y,0))
    else:
        next_state.append((a,y-(a-x)))
    
    for nx, ny in next_state:
        if (nx, ny) in visit: continue
        queue.append((nx, ny, level+1))
        visit.add((nx, ny))

if not find:
    print(-1)
else:
    print(min(answer))
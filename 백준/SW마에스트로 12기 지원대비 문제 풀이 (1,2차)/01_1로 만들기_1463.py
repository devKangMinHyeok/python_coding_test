from collections import deque
N = int(input())

queue = deque([(N,0)])
visit = set()
visit.add(N)

while queue:
    target, level = queue.popleft()
    if target == 1:
        print(level)
        break
    next_targets = []
    if target % 3 == 0: next_targets.append(target / 3)
    if target % 2 == 0: next_targets.append(target / 2)
    if target > 1: next_targets.append(target - 1)
    for next_target in next_targets:
        if next_target not in visit:
            queue.append((next_target, level+1))
            visit.add(next_target)


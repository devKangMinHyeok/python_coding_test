from collections import deque

N, K = map(int, input().split())

queue = deque([(N, 0)])
visit = set()
visit.add(N)

while queue:
    target, level = queue.popleft()
    if target == K: 
        print(level)
        break
    next_targets = [target + 1, target - 1, target * 2]
    for next_target in next_targets:
        if next_target < 0 or next_target > 100000: continue
        if next_target not in visit:
            visit.add(next_target)
            queue.append((next_target, level + 1))
            
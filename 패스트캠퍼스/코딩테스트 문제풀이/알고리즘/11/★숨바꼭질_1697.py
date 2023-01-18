from collections import deque

n, k = map(int, input().split())

def bfs (start, end):
    queue = deque([(start, 0)])
    visit = set()
    visit.add(start)
    while queue:
        val, level = queue.popleft()
        if val == end:
            return level
        for next_val in [val-1, val+1, val*2]:
            if next_val >= 0 and next_val <= 100000 and next_val not in visit:
                visit.add(next_val)
                queue.append((next_val, level+1))
            

print(bfs(n, k))
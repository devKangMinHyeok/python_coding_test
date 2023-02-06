import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
visit = set()

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

queue = deque([(1,0)])
visit.add(1)

while queue:
    target, level = queue.popleft()
    for next_target in graph[target]:
        if level == 2: continue
        if next_target not in visit:
            visit.add(next_target)
            queue.append((next_target, level+1))

print(len(visit)-1)
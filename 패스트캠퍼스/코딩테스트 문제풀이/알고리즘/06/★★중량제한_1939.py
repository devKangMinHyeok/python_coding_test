import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
max_val = 0
min_val = 100000000000
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
    max_val = max(max_val, c)
    min_val = min(min_val, c)

start, end = map(int, input().split())

low, high = min_val, max_val

def bfs(mid):
    queue = deque([start])
    visit = [False] * (n+1)
    visit[start] = True
    while queue:
        target = queue.popleft()
        for next_target, weight in graph[target]:
            if weight >= mid and not visit[next_target]:
                visit[next_target] = True
                queue.append(next_target)
    return visit[end]
                
answer = 0

while low <= high:
    mid = (low + high) // 2
    isAble = bfs(mid)
    if isAble: 
        low = mid + 1
        answer = mid
    else: high = mid - 1

print(answer)
    
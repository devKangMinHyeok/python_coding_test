import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for i in range(n+1)]
high = -1
low = 1000000000

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
    low = min(low, c)
    high = max(high, c)

start, end = map(int, input().split())
answer = low

def bfs (pivot):
    queue = deque([start])
    visit = [False] * (n+1)
    visit[start] = True
    while queue:
        target = queue.popleft()
        for (node, w) in graph[target]:
            if w >= pivot and not visit[node]:
                queue.append(node)
                visit[node] = True
    return visit[end]

while low <= high:
    mid = (low + high) // 2
    if bfs(mid):
        answer = mid
        low = mid + 1
    else:
        high = mid - 1

print(answer)
    
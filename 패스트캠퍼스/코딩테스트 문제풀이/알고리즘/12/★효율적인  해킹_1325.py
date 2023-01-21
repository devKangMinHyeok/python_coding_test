import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)

def bfs(graph, start):
    count = 1
    queue = deque([start])
    visit = [False] * (n+1)
    visit[start] = True
    
    while queue:
        target = queue.popleft()
        for next_target in graph[target]:
            if not visit[next_target]:
                count += 1
                queue.append(next_target)
                visit[next_target] = True
    return count
 
max_count = 0
answer = []
for i in range(1,n+1):
    count = bfs(graph, i)
    if count > max_count:
        answer = [i]
        max_count = count
    elif count == max_count:
        answer.append(i)
for num in answer:
    print(num, end=" ")
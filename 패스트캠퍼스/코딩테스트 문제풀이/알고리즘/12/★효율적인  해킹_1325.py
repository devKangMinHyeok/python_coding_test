import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)

def bfs(start):
    queue = deque([start])
    visit = [False] * (n+1)
    visit[start] = True
    count = 1
    
    while queue:
        target = queue.popleft()
        for next_target in graph[target]:
            if not visit[next_target]:
                visit[next_target] = True
                queue.append(next_target)
                count += 1
    return count

max_val = 1
answer = []
for i in range(1,n+1):
    counter = bfs(i)
    if counter > max_val:
        max_val = counter
        answer = [i]
    elif counter == max_val:
        answer.append(i)

for num in answer:
    print(num, end=" ")
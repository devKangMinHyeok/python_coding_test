import sys
from collections import deque
input = sys.stdin.readline

N, K, M = map(int,input().split())
graph = [[] for _ in range(N+M+1)]

def bfs (start, end):
    queue = deque([(start, 0)])
    visit = [False] * (N+M+1)
    visit[start] = True
    
    while queue:
        target, cnt = queue.popleft()
        if target == end:
            return cnt // 2 + 1
        for next_target in graph[target]:
            if not visit[next_target]:
                visit[next_target] = True
                queue.append((next_target, cnt+1))
    return -1
                
for i in range(M):
    data = list(map(int, input().split()))
    for j in range(len(data)):
        graph[data[j]].append(N+i+1)
        graph[N+i+1].append(data[j])
            
min_val = bfs(1, N)
print(min_val)
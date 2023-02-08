import sys
from collections import deque
input = sys.stdin.readline

N, M, start = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs_answer = []
bfs_answer = []

visit_dfs = [False] * (N+1)
visit_bfs = [False] * (N+1)

def dfs(x):
    visit_dfs[x] = True
    dfs_answer.append(x)
    for next_ in sorted(graph[x]):
        if not visit_dfs[next_]:
            visit_dfs[next_] = True
            dfs(next_)
        

def bfs():
    queue = deque([start])
    visit_bfs[start] = True
    
    while queue:
        target = queue.popleft()
        bfs_answer.append(target)
        for next_ in sorted(graph[target]):
            if not visit_bfs[next_]:
                queue.append(next_)
                visit_bfs[next_] = True

dfs(start)
bfs()

print(" ".join([str(i) for i in dfs_answer]))
print(" ".join([str(i) for i in bfs_answer]))
    
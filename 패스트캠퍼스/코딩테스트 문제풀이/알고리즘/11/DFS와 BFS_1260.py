import sys
from collections import deque
input = sys.stdin.readline


n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(len(graph)):
    graph[i].sort()

dfs_arr = []

def dfs (node, visit):
    global dfs_arr
    dfs_arr.append(node)
    visit[node] = True
    for next_node in graph[node]:
        if not visit[next_node]: 
            dfs(next_node, visit)

dfs(v, [False] * (n+1))

bfs_arr = []

def bfs(node):
    global bfs_arr
    queue = deque([node])
    visit = [False] * (n+1)
    while queue:
        target = queue.popleft()
        bfs_arr.append(target)
        visit[target] = True
        for next_node in graph[target]:
            if not visit[next_node]:
                visit[next_node] = True
                queue.append(next_node)

bfs(v)

print(" ".join([str(i) for i in dfs_arr]))
print(" ".join([str(i) for i in bfs_arr]))
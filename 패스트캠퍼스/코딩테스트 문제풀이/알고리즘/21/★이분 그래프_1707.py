import sys
from collections import deque
input = sys.stdin.readline

K = int(input())

def bfs(start):
    queue = deque([start])
    color[start] = 1
    
    while queue:
        target = queue.popleft()
        for next_target in graph[target]:
            if not color[next_target]:
                color[next_target] = color[target] + 1
                queue.append(next_target)

def bfs_check(start):
    queue = deque([start])
    visit = [False] * (V+1)
    visit[start] = True
    
    while queue:
        target = queue.popleft()
        for next_target in graph[target]:
            if color[next_target] == color[target]:
                return False
            if not visit[next_target]:
                visit[next_target] = True
                queue.append(next_target)
    return True
    
for _ in range(K):
    V, E = map(int, input().split())
    graph = [[] for __ in range(V+1)]
    color = [0] * (V+1)
    
    for __ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    
    answer = True
    
    for i in range(1, V+1):
        if not color[i]: 
            bfs(i)
            if not bfs_check(i):
                answer = False
                break
            
    if answer: print("YES")
    else: print("NO")
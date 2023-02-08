import sys
from heapq import heappush, heappop
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
edges = []
start = 1
end = N

for _ in range(M):
    x, y, cost = map(int, input().split())
    edges.append((x,y))
    graph[x].append((cost, y))
    graph[y].append((cost, x))

max_val = 0

def dijkstra(e_x, e_y):
    queue = []
    table = [float("inf")] * (N+1)
    table[start] = 0
    heappush(queue, (0, start))
    
    while queue:
        dist, node = heappop(queue)
        if dist > table[node]: continue
        for next_dist, next_node in graph[node]:
            if (e_x == node and e_y == next_node) or (e_x == next_node and e_y == node): continue
            if next_dist > table[next_node]: continue
            cost = dist + next_dist
            if cost < table[next_node]:
                table[next_node] = cost
                heappush(queue, (cost, next_node))
    
    return table

def back_track(table):
    queue = []
    paths = [[False] * (N+1) for _ in range(N+1)]
    heappush(queue, (table[end], end))
    
    while queue:
        dist, node = heappop(queue)
        for next_dist, next_node in graph[node]:
            v1, v2 = min(next_node, node), max(next_node, node)
            if dist - next_dist == table[next_node] and not paths[v1][v2]:
                paths[v1][v2] = True
                heappush(queue, (table[next_node], next_node))
    return paths

t = dijkstra(-1,-1)
p = back_track(t)

for i in range(N+1):
    for j in range(N+1):
        if p[i][j]:
            ta = dijkstra(i,j)
            max_val = max(max_val, ta[end])

print(max_val)
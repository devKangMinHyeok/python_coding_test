import sys
from heapq import heappush, heappop
input = sys.stdin.readline

N, E = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(E):
    a, b, cost = map(int, input().split())
    graph[a].append((cost, b))
    graph[b].append((cost, a))

v1, v2 = map(int, input().split())

def dijkstra(start, end):
    table = [float("inf")] * (N+1)
    table[start] = 0
    queue = []
    heappush(queue, (0,start))
    
    while queue:
        dist, node = heappop(queue)
        if dist > table[node]: continue
        for next_dist, next_node in graph[node]:
            cost = dist + next_dist
            if cost < table[next_node]:
                table[next_node] = cost
                heappush(queue, (cost, next_node))
    
    return table[end]

start2v1 = dijkstra(1,v1)
start2v2 = dijkstra(1,v2)
v12v2 = dijkstra(v1,v2)
v12end = dijkstra(v1,N)
v22end = dijkstra(v2,N)

answer = min(
    start2v1 + v12v2 + v22end,
    start2v2 + v12v2 + v12end
)

if answer == float("inf"): print(-1)
else: print(answer)
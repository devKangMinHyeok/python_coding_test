import sys
from heapq import heappush, heappop
input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())
graph = [[] for _ in range(V+1)]

for _ in range(E):
    u, v, cost = map(int, input().split())
    graph[u].append((cost,v))

table = [float("inf")] * (V+1)
table[K] = 0

queue = []
heappush(queue, (0,K))

while queue:
    dist, node = heappop(queue)
    for next_dist, next_node in graph[node]:
        if next_dist > table[next_node]: continue
        cost = dist + next_dist
        if cost < table[next_node]:
            table[next_node] = cost
            heappush(queue, (cost, next_node))

for i in range(1, V+1):
    if table[i] == float("inf"): print("INF")
    else: print(table[i])
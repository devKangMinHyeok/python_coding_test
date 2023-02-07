import sys
from heapq import heappush, heappop
input = sys.stdin.readline

N, M, K = map(int, input().split())
graph = [[] for _ in range(N+1)]
table = [[float("inf")] * (N+1) for _ in range(K+1)]
start = 1
end = N

for _ in range(M):
    a, b, cost = map(int, input().split())
    graph[a].append((cost,b))
    graph[b].append((cost,a))

queue = []
for i in range(K+1):
    table[i][start] = 0
heappush(queue, (0, start, 0))

while queue:
    dist, node, pozang = heappop(queue)
    if table[pozang][node] < dist: continue
    for next_dist, next_node in graph[node]:
        if pozang < K: # 포장 가능
            if dist < table[pozang+1][next_node]:
                table[pozang+1][next_node] = dist
                heappush(queue, (dist, next_node, pozang+1))
        cost = dist + next_dist
        if cost < table[pozang][next_node]:
            table[pozang][next_node] = cost
            heappush(queue, (cost, next_node, pozang))

result = float("inf")
for i in range(K+1):
    result = min(result, table[i][end])
print(result)
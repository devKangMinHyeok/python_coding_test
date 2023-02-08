import sys
from heapq import heappush, heappop
input = sys.stdin.readline

def dijkstra():
    queue = []
    table = [float("inf")] * N
    table[start] = 0
    heappush(queue, (0,start))
    
    while queue:
        dist, node = heappop(queue)
        if dist > table[node]: continue
        for i, (next_dist, next_node) in enumerate(graph[node]):
            if excepted[node][next_node]: continue
            cost = dist + next_dist
            if cost < table[next_node]:
                table[next_node] = cost
                heappush(queue, (cost, next_node))
    return table
    
def back_track(node):
    if node == start:
        return
    for i, (next_dist, next_node) in enumerate(graph_rev[node]):
        if next_dist == table[node] - table[next_node] and not excepted[next_node][node]:
            excepted[next_node][node] = True
            back_track(next_node)
    

while True:
    N, M = map(int, input().split())
    if not N and not M: break
    start, end = map(int, input().split())
    graph = [[] for _ in range(N)]
    graph_rev = [[] for _ in range(N)]
    excepted = [[False] * N for _ in range(N)]
    
    for _ in range(M):
        U, V, cost = map(int, input().split())
        graph[U].append((cost, V))
        graph_rev[V].append((cost, U))
        
    table = dijkstra()
    back_track(end)
    table = dijkstra()

    if table[end] == float("inf"): print(-1)
    else: print(table[end])
    
    
    
    
        
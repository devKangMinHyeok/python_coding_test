import sys
from heapq import heappush, heappop
from collections import deque
input = sys.stdin.readline

def daikstra():
    queue = []
    heappush(queue, (0,start))
    distance[start] = 0
    
    while queue:
        dist_cur, target = heappop(queue)
        if distance[target] < dist_cur: continue
        for (next_target, dist) in graph[target]:
            cost = distance[target] + dist
            if distance[next_target] > cost and not min_roads[target][next_target]:
                distance[next_target] = cost
                heappush(queue, (cost, next_target))

def back_track():
    queue = deque([end])
    
    while queue:
        target = queue.popleft()
        if target == start: continue
        for next_target, dist in reverse[target]:
            if dist + distance[next_target] == distance[target] and not min_roads[next_target][target]:
                queue.append(next_target)
                min_roads[next_target][target] = True

while True:
    n, m = map(int, input().split())
    if n == 0: break
    start, end = map(int, input().split())
    graph = [[] for _ in range(n)]
    reverse = [[] for _ in range(n)]
    for _ in range(m):
        u, v, p = map(int, input().split())
        graph[u].append((v,p))
        reverse[v].append((u,p))
    min_roads = [[False]*(n) for _ in range(n)]
    distance = [float("inf")] * (n)
    daikstra()
    back_track()
    distance = [float("inf")] * (n)
    daikstra()

    if distance[end] == float("inf"): print(-1)
    else: print(distance[end])
    
    
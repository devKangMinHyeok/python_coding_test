import sys
from heapq import heappush, heappop
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n, d, c = map(int, input().split())
    graph = [[] for i in range(n+1)]
    distance = [float("inf")] * (n+1)
    
    for _ in range(d):
        a, b, s = map(int, input().split())
        graph[b].append((s,a))
    
    queue = []
    heappush(queue, (0,c))
    distance[c] = 0
    
    while queue:
        dist, target = heappop(queue)
        if dist > distance[target]: continue
        for next_dist, next_target in graph[target]:
            if dist + next_dist < distance[next_target]:
                distance[next_target] = dist + next_dist
                heappush(queue, (distance[next_target], next_target))
    
    count = 0
    max_val = 0
    for i in range(len(distance)):
        if distance[i] != float("inf"):
            count += 1
            max_val = max(max_val, distance[i])
    print(count, max_val)
    
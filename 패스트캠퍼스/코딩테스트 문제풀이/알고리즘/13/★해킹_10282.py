import sys
from heapq import heappush, heappop
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n, d, c = map(int, input().split())
    graph = [[] for __ in range(n+1)]
    distance = [float("inf")] * (n+1)
    for __ in range(d):
        a, b, s = map(int, input().split())
        graph[b].append((a,s))
    distance[c] = 0
    queue = []
    heappush(queue, c)
    while queue:
        target = heappop(queue)
        for next_target, dist in graph[target]:
            if distance[next_target] > distance[target] + dist:
                distance[next_target] = distance[target] + dist
                heappush(queue, next_target)
    counter = 0
    max_time = 0
    for num in distance:
        if num != float("inf"):
            counter += 1
            max_time = max(max_time, num)
    print(counter, max_time)
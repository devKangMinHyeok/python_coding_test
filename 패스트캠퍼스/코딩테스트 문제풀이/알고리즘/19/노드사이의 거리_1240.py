import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
targets = []
answer = []

for _ in range(n-1):
    a, b, dist = map(int, input().split())
    graph[a].append((b, dist))
    graph[b].append((a, dist))

for _ in range(m):
    a, b = map(int, input().split())
    targets.append((a,b))

def get_distance (start, end):
    distance = [float("inf")] * (n+1)
    distance[start] = 0
    queue = []
    heappush(queue, (0, start))
    
    while queue:
        dist, target = heappop(queue)
        if dist > distance[target]: continue
        for next_target, next_dist in graph[target]:
            cost = distance[target] + next_dist
            if distance[next_target] > cost:
                distance[next_target] = cost
                heappush(queue, (distance[next_target], next_target))
    return distance[end]

for start, end in targets:
    print(get_distance(start, end))


"""
신장트리에서는 사이클이 없기 때문에, 특정 노드에서 특정 노드로 가는 길은 오직 하나다.
"""
import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for i in range(n+1)]
in_degree = [0 for i in range(n+1)]
in_degree[0] = -1
answer = []

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    in_degree[b] += 1

queue = []
for i, num in enumerate(in_degree):
    if num == 0:
        heappush(queue, i)
        in_degree[i] = -1

while queue:
    target = heappop(queue)
    answer.append(target)
    next = graph[target]
    for num in next:
        in_degree[num] -= 1
        if in_degree[num] == 0:
            heappush(queue, num)
            in_degree[num] = -1

print(" ".join([str(i) for i in answer]))
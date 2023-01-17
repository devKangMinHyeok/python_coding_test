import sys
from heapq import heappush, heappop

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
indegree = [0 for _ in range(n+1)]
pqueue = []

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

for i in range(1, n+1):
    if indegree[i] == 0: heappush(pqueue, i)

while pqueue:
    target = heappop(pqueue)
    print(target, end=" ")
    for num in graph[target]:
        indegree[num] -= 1
        if not indegree[num]: heappush(pqueue, num)
        

""" Union-find 풀이
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

parent = [i for i in range(n+1)]

def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]

def union(a,b):
    a = find(a)
    b = find(b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

for _ in range(m):
    a, b = map(int, input().split())
    union(a,b)

answer = -1

for i in range(1,len(parent)):
    parent[i] = find(i)

for num in parent:
    if num == 1: answer += 1

print(answer)
"""

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

queue = deque([1])
visit = [False] * (n+1)
visit[1] = True
answer = 0

while queue:
    target = queue.popleft()
    for next_target in graph[target]:
        if not visit[next_target]:
            queue.append(next_target)
            visit[next_target] = True
            answer += 1

print(answer)


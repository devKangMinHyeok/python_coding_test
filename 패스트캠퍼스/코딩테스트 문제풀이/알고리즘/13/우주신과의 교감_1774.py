import sys
from heapq import heappush, heappop
input = sys.stdin.readline

def get_dist (a,b):
    x1,y1 = a
    x2,y2 = b
    return ((x1-x2)**2 + (y1-y2)**2)**(1/2)

def find (x):
    if parent[x] == x: return x
    else:
        parent[x] = find(parent[x])
        return parent[x]

def union (a,b):
    a = find(a)
    b = find(b)
    if a < b: parent[b] = a
    else: parent[a] = b

n, m = map(int, input().split())
place = [(0,0)]
parent = [i for i in range(n+1)]

for _ in range(n):
    x, y = map(int, input().split())
    place.append((x,y))
    
for _ in range(m):
    a, b = map(int, input().split())
    union(a,b)

heap = []

for i in range(1,len(place)):
    for j in range(i+1, len(place)):
        heappush(heap, (get_dist(place[i], place[j]), (i,j)))

answer = 0

while heap:
    dist, (i, j) = heappop(heap)
    if find(i) != find(j): 
        answer += dist
        union(i,j)

print("%0.2f" % answer)

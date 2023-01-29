import sys
from heapq import heappush, heappop
input = sys.stdin.readline

def get_dist(a,b):
    return ((a[0]-b[0])**2 + (a[1]-b[1])**2)**(1/2)

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
place = []
parent = [i for i in range(n+1)]

for _ in range(n):
    x, y = map(int, input().split())
    place.append((x,y))
    
for _ in range(m):
    a, b = map(int, input().split())
    union(a,b)

lines = []

for i in range(len(place)):
    for j in range(i+1,len(place)):
        heappush(lines, (get_dist(place[i], place[j]), (i+1,j+1))) 

answer = 0

while lines:
    dist, (a, b) = heappop(lines)
    if find(a) == find(b): continue
    union(a,b)
    answer += dist

print("%.2f" % answer)
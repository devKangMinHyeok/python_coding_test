import sys
input = sys.stdin.readline

n, m = map(int, input().split())

parent = [i for i in range(n+1)]

def find(x):
    if x != parent[x]: parent[x] = find(parent[x])
    return parent[x]

def union(y,x):
    y = find(y)
    x = find(x)
    if (y > x): parent[y] = x
    else: parent[x] = y

for _ in range(m):
    n1, n2 = map(int, input().split())
    union(n1,n2)
    
for i in range(1,n+1):
    find(i)
    
print(len(set(parent[1:])))

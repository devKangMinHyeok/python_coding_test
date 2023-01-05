import sys
input = sys.stdin.readline

n, m = map(int, input().split())

parent = [i for i in range(n)]

def find(x):
    if x != parent[x]: parent[x] = find(parent[x])
    return parent[x]

def union(y,x):
    y = find(y)
    x = find(x)
    if y > x: parent[y] = x
    else : parent[x] = y

for i in range(1,m+1):
    p1, p2 = map(int, input().split())
    
    if find(p1) == find(p2):
        print(i)
        exit(0)
    else:
        union(p1,p2)
print(0)
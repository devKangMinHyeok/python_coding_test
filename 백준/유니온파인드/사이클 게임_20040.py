import sys
input = sys.stdin.readline

n, m = map(int, input().split()) # n 점의 개수, m 진행된 차례의 수

parent = [i for i in range(n)]

def find(x):
    if x == parent[x] : return x
    else :
        parent[x] = find(parent[x])
        return parent[x]

def union(y,x):
    y = find(y)
    x = find(x)
    if (x < y) : parent[y] = x
    else : parent[x] = y

for i in range(m):
    p1, p2 = map(int, input().split())
    if (find(p1) == find(p2)) : 
        print(i+1)
        exit(0)
    else :
        union(p1, p2)

print(0)


import sys
input = sys.stdin.readline

n, m = map(int, input().split())

table = [i for i in range(n+1)]

def find (x):
    if (table[x] == x): return x
    else: 
        table[x] = find(table[x])
        return table[x]
    
def union (y,x):
    y = find(y)
    x = find(x)
    table[x] = y

for _ in range(m):
    types, a, b = map(int, input().split())
    if (types):
        if find(a) == find(b): print("YES")
        else : print("NO")
    else :
        union(a,b)
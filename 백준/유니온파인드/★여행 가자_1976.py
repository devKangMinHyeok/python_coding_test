import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

table = [i for i in range(n+1)]

def find (x) :
    if (table[x] == x): return x
    else:
        table[x] = find(table[x])
        return table[x]
    
def union (y,x):
    y = find(y)
    x = find(x)
    if (y < x): table[x] = y
    else: table[y] = x

for i in range(n):
    data = list(map(int, input().split()))
    for j, num in enumerate(data):
        if num : union(i+1,j+1)

plan = list(map(int, input().split()))

for i in range(len(plan)-1):
    if table[plan[i]] == table[plan[i+1]]: continue
    else :
        print("NO")
        exit(0)
        
print("YES")        

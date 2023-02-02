import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
T = int(input())
    
def isCycle (node):
    global cnt
    cycle.append(node)
    visit[node] = True
    next_node = edges[node]
    if visit[next_node]:
        if next_node in cycle:
            start = cycle.index(next_node)
            cnt += len(cycle[start:])
        return
    else: 
        isCycle(next_node)

for _ in range(T):
    n = int(input())
    edges = list(map(int, input().split()))
    edges.insert(0, -1)
    visit = [False] * (n+1)
    cnt = 0
    for i in range(1, len(edges)):
        if not visit[i]:
            cycle = []
            isCycle(i)
    print(n - cnt)
    
        
import sys
input = sys.stdin.readline

while True:
    n, m = map(int, input().split())
    if not n and not m: break
    s, d = map(int, input().split())
    graph = [[] for _ in range(n)]
    distance = [float("inf")] * n
    
    for _ in range(m):
        u, v, p = map(int, input().split())
        graph[u].append((p,v))

    
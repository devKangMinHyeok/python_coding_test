import sys
input = sys.stdin.readline

def dfs(x, acc):
    global min_length
    if len(visit) == N and graph[x][start]:
        min_length = min(min_length, acc + graph[x][start])
    for i, cost in enumerate(graph[x]):
        if i == x: continue
        if i in visit: continue
        if cost == 0: continue
        visit.add(i)
        dfs(i, acc+cost)
        visit.remove(i)
        

N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

min_length = float("inf") 

for i in range(N):
    start, end = i, i
    starting = True
    visit = set()
    visit.add(start)
    dfs(start, 0)

print(min_length)
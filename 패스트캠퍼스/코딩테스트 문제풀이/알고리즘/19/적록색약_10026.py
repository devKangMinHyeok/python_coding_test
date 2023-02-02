import sys
sys.setrecursionlimit(10000)
n = int(input())
graph = []
visit = [[False] * n for _ in range(n)]

answer1 = 0
answer2 = 0

for i in range(n):
    line = list(input())
    graph.append(line)

def dfs (y, x, target):
    for dy, dx in [(1,0), (0,1), (-1,0), (0, -1)]:
        ny, nx = dy + y, dx + x
        if ny < 0 or nx < 0 or ny >= n or nx >= n: continue
        if visit[ny][nx] or target != graph[ny][nx]: continue
        visit[ny][nx] = True
        dfs(ny, nx, target)

def search ():
    answer = 0
    for i in range(n):
        for j in range(n):
            if not visit[i][j]:
                target = graph[i][j]
                visit[i][j] = True
                answer += 1
                dfs(i, j, target)
    return answer

answer1 = search()

visit = [[False] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if graph[i][j] == "R":
            graph[i][j] = "G"

answer2 = search()

print(answer1, answer2)
n = int(input())
graph = []
visit = [[False] * n for _ in range(n)]
answer = []

for i in range(n):
    line = list(input())
    graph.append([int(i) for i in line])

def dfs (y, x):
    cnt = 1
    for dy, dx in [(-1,0), (0,1), (1,0), (0, -1)]:
        ny, nx = dy + y, dx + x
        if ny < 0 or nx < 0 or ny >= n or nx >= n: continue
        if not graph[ny][nx] or visit[ny][nx]: continue
        visit[ny][nx] = True
        cnt += dfs(ny,nx)
    return cnt

for i in range(n):
    for j in range(n):
        if graph[i][j] and not visit[i][j]:
            visit[i][j] = True
            cnt = dfs(i,j)
            answer.append(cnt)

answer.sort()
print(len(answer))
for i in answer:
    print(i)
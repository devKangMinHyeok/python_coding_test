R, C = map(int, input().split())
graph = []
for _ in range(R):
    graph.append(input())

max_len = 0
visit = [False] * (ord('Z')+1)
def dfs(y,x,cnt):
    global max_len
    max_len = max(max_len, cnt)
    for dy, dx in [(1,0), (0,1), (-1,0), (0,-1)]:
        ny, nx = dy + y, dx + x
        if ny < 0 or nx < 0 or ny >= R or nx >= C: continue
        if not visit[ord(graph[ny][nx])]:
            visit[ord(graph[ny][nx])] = True
            dfs(ny,nx,cnt+1)
            visit[ord(graph[ny][nx])] = False
    
visit[ord(graph[0][0])] = True
dfs(0,0,1)

print(max_len)
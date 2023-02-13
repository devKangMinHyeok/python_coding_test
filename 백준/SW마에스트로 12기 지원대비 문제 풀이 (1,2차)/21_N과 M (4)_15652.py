N, M = map(int, input().split())

def dfs(x, arr):
    if len(arr) == M:
        print(" ".join(map(str, arr)))
        return
    for i in range(x, N+1):
        arr.append(i)
        dfs(i, arr)
        arr.pop()
dfs(1, [])

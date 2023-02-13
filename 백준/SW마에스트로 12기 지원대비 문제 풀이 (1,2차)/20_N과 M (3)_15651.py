N, M = map(int, input().split())
data = [i for i in range(1, N+1)]

def dfs(arr):
    if len(arr) == M:
        print(" ".join(map(str, arr)))
        return
    for i in range(1, N+1):
        arr.append(i)
        dfs(arr)
        arr.pop()

dfs([])

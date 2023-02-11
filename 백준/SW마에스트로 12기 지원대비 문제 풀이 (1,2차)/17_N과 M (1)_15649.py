# dfs 풀이
N, M = map(int, input().split())

def dfs(path):
    if len(path) == M:
        print(" ".join(str(i) for i in path))
        return
    for i in range(1,N+1):
        if i in path: continue
        path.append(i)
        dfs(path)
        path.pop()

dfs([])


"""
# itertools 풀이
from itertools import permutations

N, M = map(int, input().split())
data = [i for i in range(1, N+1)]
result = permutations(data, M)
for res in result:
    for i in res:
        print(i, end=" ")
    print("")
"""
N, M = map(int, input().split())
data = [i for i in range(1, N+1)]
answer = set()
def dfs(arr):
    if len(arr) == M:
        answer.add(tuple(sorted(arr[:])))
        return
    for i in range(1,N+1):
        if i not in arr:
            arr.append(i)
            dfs(arr)
            arr.pop()
        
dfs([])
answer = list(answer)
answer.sort()
for ans in answer:
    for i in ans:
        print(i, end=" ")
    print("")




"""
# itertools 사용 풀이
from itertools import combinations

N, M = map(int, input().split())
data = [i for i in range(1,N+1)]
result = combinations(data, M)
for res in result:
    for i in res:
        print(i, end=" ")
    print("")
"""
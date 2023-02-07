# python combination 풀이
from itertools import combinations

L, C = map(int, input().split())
data = list(map(str, input().split()))
data.sort()

for pw in combinations(data, L):
    mo = 0
    for moem in ['a','e','i','o','u']:
        if moem in pw: mo += 1
    za = L - mo
    if mo >= 1 and za >= 2:
        print("".join(pw))

"""
# 백트랙킹 풀이

L, C = map(int, input().split())
data = list(map(str, input().split()))

def dfs(x, crypto):
    if x >= C: return
    if len(crypto) == L:
        mo = 0
        for moem in ['a','e','i','o','u']:
            if moem in crypto: mo += 1
        za = L - mo
        if mo >= 1 and za >= 2:
            print(crypto)
            return
    for i in range(x+1, C):
        dfs(i, crypto + data[i])
    
data.sort()
for i in range(C):
    dfs(i, data[i])

"""
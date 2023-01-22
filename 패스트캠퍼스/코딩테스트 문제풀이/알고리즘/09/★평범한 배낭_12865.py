"""
4 7
[(6,13), (4,8), (3,6), (5,12)]
=> [(3,6), (4,8), (5,12), (6,13)]

    0   1   2   3   4   5   6   7
0   0   0   0   0   0   0   0   0
1   0   0   0   6   6   6   6   6
2   0   0   0   6   8   8   8   14
3   0   0   0   6   8   12  12  14
4   0   0   0   6   8   12  13  14
"""


import sys
input = sys.stdin.readline

n, k = map(int, input().split())
data = []

for _ in range(n):
    w, v = map(int, input().split())
    data.append((w,v))

data.sort()

dp = [[0 for _ in range(k+1)] for __ in range(n+1)]

for i in range(1,n+1):
    w, v = data[i-1]
    for j in range(1,k+1):
        if j < w: dp[i][j] = dp[i-1][j]
        else: dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + v)

print(max(dp[-1]))
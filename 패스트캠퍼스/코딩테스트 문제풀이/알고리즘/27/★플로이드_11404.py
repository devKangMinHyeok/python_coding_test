import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
DP = [[float("inf")] * (n+1) for _ in range(n+1)]

for _ in range(m):
    a, b, cost = map(int, input().split())
    DP[a][b] = min(DP[a][b], cost)

for i in range(1,n+1):
    DP[i][i] = 0

for i in range(1,n+1):
    for j in range(1,n+1):
        for k in range(1,n+1):
            DP[j][k] = min(DP[j][k], DP[j][i] + DP[i][k])

for i in range(1, n+1):
    for j in range(1, n+1):
        if DP[i][j] == float("inf"): print(0, end=" ")
        else: print(DP[i][j], end=" ")
    print("")
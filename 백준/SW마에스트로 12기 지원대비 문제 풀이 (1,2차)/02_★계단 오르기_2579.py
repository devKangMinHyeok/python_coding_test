import sys
input = sys.stdin.readline

n = int(input())
stairs = []
for _ in range(n):
    stairs.append(int(input()))

DP = [-1] * n
DP[0] = stairs[0]
if n > 1:
    DP[1] = stairs[0] + stairs[1]
if n > 2:
    DP[2] = max(stairs[2] + stairs[1], stairs[2] + stairs[0])

for i in range(3, n):
    DP[i] = max(stairs[i] + stairs[i-1] + DP[i-3], stairs[i] + DP[i-2])

print(DP[n-1])
import sys
input = sys.stdin.readline

n = int(input())
stairs = []
for _ in range(n):
    stairs.append(int(input()))

DP = [0] * n
DP[0] = stairs[0]
if n == 1: 
    print(DP[0])
    exit(0)
DP[1] = stairs[0] + stairs[1]
if n == 2:
    print(DP[1])
    exit(0)
DP[2] = stairs[2]+ max(stairs[0], stairs[1])

for i in range(3, n):
    DP[i] = stairs[i] + max(DP[i-2], stairs[i-1] + DP[i-3])

print(DP[n-1])


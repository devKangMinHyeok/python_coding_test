import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n, k = map(int, input().split())
org_coins = []

for _ in range(n):
    num = int(input())
    org_coins.append(num)

DP = [0] * (k+1)
org_coins.sort()
DP[0] = 1

for c in org_coins:
    for i in range(c, k+1):
        DP[i] += DP[i-c]

print(DP[k])


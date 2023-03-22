import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = []
coins.sort()

for _ in range(n): coins.append(int(input()))

DP = [0] * (k+1)
DP[0] = 1

for coin in coins:
    for j in range(coin, k+1):
        DP[j] += DP[j-coin]

print(DP[k])
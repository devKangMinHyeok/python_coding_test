import sys
input = sys.stdin.readline

n, W = map(int, input().split())
prices = []
for _ in range(n):
    prices.append(int(input()))

for i in range(n-1):
    today = prices[i]
    tomo = prices[i+1]
    if today < tomo:
        coins = W // today
        W = W % today
        W += coins * tomo
        coins = 0

print(W)
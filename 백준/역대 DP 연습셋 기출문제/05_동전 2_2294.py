import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
coins = []

for _ in range(n):
    coins.append(int(input()))
    
coins = list(set(coins))
coins.sort()

visit = set()

queue = deque([])
for coin in coins:
    queue.append((coin, 1))
    visit.add(coin)

while queue:
    target, dist = queue.popleft()
    if target == k:
        print(dist)
        exit(0)
        
    for coin in coins:
        if target + coin > k: continue
        if target + coin in visit: continue
        queue.append((target+coin, dist + 1))
        visit.add(target+coin)

print(-1)

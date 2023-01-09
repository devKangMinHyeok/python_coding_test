import sys
from heapq import heapify, heappush, heappop
input = sys.stdin.readline

k, n = map(int, input().split())
primes = list(map(int, input().split()))
min_heap = [i for i in primes]
visited = set()
heapify(min_heap)
answer = -1
max_value = max(primes)

for i in range(n):
    answer = heappop(min_heap)
    for prime in primes:
        target = prime * answer
        if len(min_heap) > n and target > max_value: continue
        if target not in visited:
            heappush(min_heap, target)
            visited.add(target)
            if target > max_value: max_value = target

print(answer)

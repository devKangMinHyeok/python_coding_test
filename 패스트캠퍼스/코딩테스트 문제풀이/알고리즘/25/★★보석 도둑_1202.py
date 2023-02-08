import sys
from heapq import heappush, heappop
input = sys.stdin.readline

N, K = map(int, input().split())
stones = []
bags = []

for _ in range(N):
    M, V = map(int, input().split())
    heappush(stones, (M,V))
    
for _ in range(K):
    C = int(input())
    bags.append(C)

bags.sort()
heap = []
answer = 0

for bag in bags:
    while stones and bag >= stones[0][0]:
        weight, value = heappop(stones)
        heappush(heap, -value)
    if heap:
        answer += heappop(heap)

print(-answer)
    
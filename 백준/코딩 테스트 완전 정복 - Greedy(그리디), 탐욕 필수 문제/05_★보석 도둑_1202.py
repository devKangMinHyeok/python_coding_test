import sys
from heapq import heappush, heappop
input = sys.stdin.readline

N, K = map(int, input().split())
rubys = []
bags = []

for _ in range(N):
    M, V = map(int, input().split())
    heappush(rubys, (M,V))

for _ in range(K):
    C = int(input())
    bags.append(C)

bags.sort()

heap = []
answer = 0

for bag in bags:
    while rubys and rubys[0][0] <= bag:
        M, V = heappop(rubys)
        heappush(heap, -V)
    if heap: answer += -heappop(heap)

print(answer)

    
        

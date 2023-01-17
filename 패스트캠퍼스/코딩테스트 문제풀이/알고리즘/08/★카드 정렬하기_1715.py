import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n = int(input())
min_heap = []
answer = 0

for _ in range(n):
    heappush(min_heap, int(input()))

while len(min_heap) > 1:
    result = heappop(min_heap) + heappop(min_heap)
    heappush(min_heap, result)
    answer += result

print(answer)
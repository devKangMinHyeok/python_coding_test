from heapq import heappush, heappop
import sys
input = sys.stdin.readline

n = int(input())
min_heap = []

for _ in range(n):
    heappush(min_heap, int(input()))

sum = 0

while len(min_heap) > 1:
    two_sum = heappop(min_heap) + heappop(min_heap)
    sum += two_sum
    heappush(min_heap, two_sum)
    
print(sum)

    
    


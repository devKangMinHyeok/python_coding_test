import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n = int(input())
min_heap = []

for _ in range(n):
    num = int(input())
    heappush(min_heap, num)

for _ in range(n):
    print(heappop(min_heap))



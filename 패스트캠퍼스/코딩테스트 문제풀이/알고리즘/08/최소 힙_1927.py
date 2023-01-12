from heapq import heappush, heappop
import sys
input = sys.stdin.readline

n = int(input())
min_heap = []

for _ in range(n):
    num = int(input())
    if not num: 
        if min_heap: print(heappop(min_heap))
        else: print(0)
    else:
        heappush(min_heap, num)

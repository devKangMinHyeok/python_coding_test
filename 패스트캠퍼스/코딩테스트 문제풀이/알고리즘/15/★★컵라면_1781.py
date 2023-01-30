import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n = int(input())
schedule = []
for _ in range(n):
    dead, cup = map(int, input().split())
    schedule.append((dead, cup))

schedule.sort(key=lambda x: -x[0])
min_heap = []

while schedule:
    dead, cup = schedule.pop()
    heappush(min_heap, cup)
    if dead < len(min_heap):
        heappop(min_heap)

print(sum(min_heap))
    
    
        
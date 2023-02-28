import sys
from heapq import heappush, heappop
input = sys.stdin.readline

N = int(input())
cups = []
for _ in range(N):
    dead, cup = map(int, input().split())
    cups.append((dead, cup))

cups.sort(key = lambda x : (x[0], x[1]))

heap = []

for dead, cup in cups:
    heappush(heap, cup)
    if len(heap) > dead:
       heappop(heap)

print(sum(heap))

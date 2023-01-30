import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n = int(input())
cups = []
for _ in range(n):
    dead, cup = map(int, input().split())
    heappush(cups, (dead, cup))

heap = []

while cups:
    dead, cup = heappop(cups)
    heappush(heap, cup)
    if len(heap) > dead:
        heappop(heap)

print(sum(heap))
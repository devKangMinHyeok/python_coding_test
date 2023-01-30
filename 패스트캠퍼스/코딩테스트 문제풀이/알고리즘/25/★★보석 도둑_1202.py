import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n, k = map(int, input().split())
golds = []
bags = []

for _ in range(n):
    weight, value = map(int, input().split())
    golds.append((weight, value))

for _ in range(k):
    max_weight = int(input())
    bags.append(max_weight)

golds.sort()
bags.sort()

heap = []
i = 0
answer = 0

for bag in bags:
    while i < len(golds) and golds[i][0] <= bag:
        heappush(heap, -golds[i][1])
        i += 1
    if heap: answer += -heappop(heap)

print(answer)    
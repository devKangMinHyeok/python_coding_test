import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n = int(input())
heap = []
answer = []

for _ in range(n):
    target = int(input())
    if target:
        if target > 0: heappush(heap, (target, target))
        else: heappush(heap, (abs(target)-0.1, target))
    else:
        if heap: answer.append(heappop(heap))
        else: answer.append((0,0))

for ans in answer:
    print(ans[1])

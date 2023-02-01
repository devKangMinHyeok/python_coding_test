import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n = int(input())
lines = []

for _ in range(n):
    a, b = map(int, input().split())
    heappush(lines, (a, b))

sum = 0

while lines:
    first = heappop(lines)
    if not lines: sum += first[1]-first[0]
    else:
        second = heappop(lines)
        if first[1] >= second[0]:
            heappush(lines, (first[0], max(first[1], second[1])))
        else:
            heappush(lines, second)
            sum += first[1]-first[0]

print(sum)
        


import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n = int(input())
lines = []
for _ in range(n):
    home, office = map(int, input().split())
    lines.append((min(home, office), max(office, home)))
L = int(input())

lines.sort(key = lambda x : x[1])

container = []
max_val = 0

for start, end in lines:
    if end - start > L: continue
    heappush(container, start)
    while container and container[0] < end - L:
        heappop(container)
    max_val = max(max_val, len(container))

print(max_val)
        

        
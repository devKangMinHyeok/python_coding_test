import sys
from heapq import heappush, heappop
input = sys.stdin.readline

N = int(input())
station = []

for _ in range(N):
    a, b = map(int, input().split())
    station.append((a,b))
    
L, fuel = map(int, input().split())

station.sort()
station.append((L,0))
max_heap = []
prev_dist = 0
answer = 0

for dist, adder in station:
    fuel -= dist - prev_dist
    prev_dist = dist
    
    while fuel < 0:
        if max_heap: 
            max_fuel = -heappop(max_heap)
            fuel += max_fuel
            answer += 1
        else: 
            print(-1)
            exit(0)
    heappush(max_heap, -adder)
    
print(answer)
    

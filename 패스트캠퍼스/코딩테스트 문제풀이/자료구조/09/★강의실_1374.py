import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n = int(input())
answer = 1
lectures = []
for _ in range(n):
    num, start, end = map(int, input().split())
    heappush(lectures, (start, end))

room = []
heappush(room, heappop(lectures)[1])

while lectures:
    end = heappop(room)
    new_start, new_end = heappop(lectures)
    if end > new_start:
        heappush(room, end)
        heappush(room, new_end)
        answer += 1
    else:
        heappush(room, new_end)
        
print(answer) 
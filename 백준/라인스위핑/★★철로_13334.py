import sys
from heapq import heappop, heappush
input = sys.stdin.readline

n = int(input())
data = []
for _ in range(n):
    h, o = map(int, input().split())
    data.append((min(h,o), max(h,o)))
d = int(input())
new_data = []
for i, (h,o) in enumerate(data):
    if o-h <= d:
        new_data.append((h,o))
data = new_data
data.sort(key=lambda x : (x[1], x[0]))

heap = []
answer = 0

for (h, o) in data:
    if not heap:
        heappush(heap, (h,o))
    else:
        while heap and o - min(heap[0][0], h) > d: # 제한 크기를 넘는 경우
            answer = max(answer, len(heap))
            heappop(heap)
        heappush(heap,(h,o))


print(max(answer, len(heap)))
            
        
import sys
from heapq import heappush, heappop
input = sys.stdin.readline

N = int(input())
max_heap = []
max_heap_neg = []
for _ in range(N):
    num = int(input())
    if num < 0: heappush(max_heap_neg, num)
    else: heappush(max_heap, -num)

answer = 0

while len(max_heap) >= 2:
    a, b = -heappop(max_heap), -heappop(max_heap)
    if a * b > a + b:
        answer += a * b
    else:
        answer += a
        heappush(max_heap, -b)

while len(max_heap_neg) >= 2:
    a, b = heappop(max_heap_neg), heappop(max_heap_neg)
    answer += a * b
    
if max_heap_neg:
    a = heappop(max_heap_neg)
    if max_heap:
        b = -heappop(max_heap)
        if a * b > a + b:
            answer += a * b
        else:
            answer += a + b
    else:
        answer += a

if max_heap:
    answer += -heappop(max_heap)

print(answer)





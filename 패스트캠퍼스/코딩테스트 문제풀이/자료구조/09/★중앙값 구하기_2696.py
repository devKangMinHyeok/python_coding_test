import sys
from heapq import heappop, heappush
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    answer = []
    max_heap = []
    mid_val = 0
    min_heap = []
    
    m = int(input())
    data = []
    for _ in range(m//10 + 1):
        data += list(map(int, input().split()))
    mid_val = data[0]
    answer.append(mid_val)
    
    for i in range(1, len(data)):
        num = data[i]
        if num <= mid_val: heappush(max_heap, (-num, num))
        else: heappush(min_heap, (num, num))
        if i % 2 == 0:
            while len(max_heap) > len(min_heap):
                heappush(min_heap, (mid_val, mid_val))
                mid_val = heappop(max_heap)[1]
            while len(min_heap) > len(max_heap):
                heappush(max_heap, (-mid_val, mid_val))
                mid_val = heappop(min_heap)[1]
            answer.append(mid_val)
    print(len(answer))
    for i , num in enumerate(answer):
        print(num, end=" ")
        if i % 10 == 9: 
            print("")
        
            
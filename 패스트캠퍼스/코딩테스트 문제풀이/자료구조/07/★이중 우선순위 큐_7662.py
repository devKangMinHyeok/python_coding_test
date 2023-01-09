import sys
from heapq import heappush, heappop
input = sys.stdin.readline

T = int(input())

def pop (heap):
    while heap:
        num, index = heappop(heap)
        if not deleted[index]:
            deleted[index] = True
            return num
    return None

for _ in range(T):
    k = int(input())
    max_heap = []
    min_heap = []
    deleted = [False] * (k+1) 
    index = 0
    
    for __ in range(k):
        cmd, num = map(str, input().split())
        num = int(num)
        
        if cmd == "I":
            heappush(max_heap, (-num, index))
            heappush(min_heap, (num, index))
            index += 1
        else:
            if num == 1:
                pop(max_heap)
            else:
                pop(min_heap)
    
    # max_val = pop(max_heap)
    # min_val = pop(min_heap)
    # if max_val and min_val: print(-max_val, min_val)
    # else: print("EMPTY")
    max_value = pop(max_heap)
    if max_value == None: print("EMPTY")
    else:
        heappush(min_heap, (-max_value, index))
        print(-max_value, pop(min_heap))
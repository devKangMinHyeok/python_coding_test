# 2:40 - 
from heapq import heappush, heappop, heapify ,nsmallest
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    k = int(input())
    queue = []
    for i in range(k):
        command, num = map(str, input().split())
        num = int(num)
        if command == "I":
            heappush(queue, num)
        else :
            if not queue: continue
            if num == 1: 
                queue = nsmallest(len(queue)-1, queue)
                heapify(queue)
            else : 
                heappop(queue)
    if queue:
        print(queue[-1], queue[0])
    else:
        print("EMPTY")


from heapq import heappop, heappush, nsmallest
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    m = int(input())
    heap = []
    answer = []
    data = []
    for i in range((m // 10)+1): data += list(map(int, input().split()))
    for i ,num in enumerate(data):
        heappush(heap, num)
        if (i+1) % 2: # odd
            mid_index = (i+1) // 2
            answer.append(str(nsmallest(mid_index+1, heap)[-1]))
    print(len(answer))
    for i, num in enumerate(answer):
        print(num, end=" ")
        if i % 10 == 9: print("")
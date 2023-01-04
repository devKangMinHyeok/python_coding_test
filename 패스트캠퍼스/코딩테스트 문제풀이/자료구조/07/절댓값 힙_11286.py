import sys
input = sys.stdin.readline
from queue import PriorityQueue

n = int(input())
queue = PriorityQueue()
answer = []

for _ in range(n):
    num = int(input())
    if num == 0:
        if (queue.empty()): answer.append("0")
        else : answer.append(str(queue.get()[1]))
    elif num > 0:
        queue.put((num, num))
    else :
        queue.put((abs(num)-0.1, num))

print("\n".join(answer))
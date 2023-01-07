from collections import deque

n, k = map(int, input().split())
data = [i for i in range(1,n+1)]
deq = deque(data)
answer = []

while deq:
    for _ in range(k-1):
        deq.rotate(-1)
    answer.append(str(deq.popleft()))

answer = ", ".join(answer)
print("<"+answer+">")
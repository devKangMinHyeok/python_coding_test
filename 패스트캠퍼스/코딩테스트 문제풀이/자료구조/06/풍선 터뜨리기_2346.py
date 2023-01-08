from collections import deque

n = int(input())
data = list(map(int, input().split()))
queue = deque([(i+1,num) for i, num in enumerate(data)])
answer = []

while queue:
    i, target = queue.popleft()
    answer.append(str(i))
    if target > 0:
        for _ in range(target-1): queue.rotate(-1)
    else:
        for _ in range(abs(target)): queue.rotate(1)

print(" ".join(answer))
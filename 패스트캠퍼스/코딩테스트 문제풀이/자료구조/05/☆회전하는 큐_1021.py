from collections import deque

n, m = map(int, input().split())
targets = list(map(int, input().split()))
deque = deque([i for i in range(1,n+1)])
count = 0

while targets:
    target = targets[0]
    target_index = deque.index(target)
    pivot = len(deque) / 2
    if (target_index > pivot) :
        while target != deque[0]:
            deque.rotate(1)
            count += 1
        deque.popleft()
    else : 
        while target != deque[0]:
            deque.rotate(-1)
            count += 1
        deque.popleft()
    del targets[0]

print(count)


"""
[1,2,3,[4],5,6]
 6/2 = 3
[1,2,3,[4],5] 
5/2 = 2.5
pivot 보다 크면 right rotation
"""
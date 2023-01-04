n = int(input())
queue = list(map(int, input().split(" ")))
queue = [(i, num) for i, num in enumerate(queue)]
answer = []
while (queue) :
    target = queue.pop(0)
    answer.append(str(target[0]+1))
    if not queue: break
    if target[1] > 0:
        for _ in range(target[1]-1):
            queue.append(queue.pop(0))
    else :
        for _ in range(abs(target[1])):
            queue.insert(0, queue.pop())
print(" ".join(answer))
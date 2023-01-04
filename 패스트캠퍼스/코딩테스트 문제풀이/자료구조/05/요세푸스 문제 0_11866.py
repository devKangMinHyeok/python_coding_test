n, k = map(int, input().split())
queue = [i for i in range(1,n+1)]
answer = []
while (queue) :
    for _ in range(k-1):
        queue.append(queue.pop(0))
    answer.append(str(queue.pop(0)))
answer = ", ".join(answer)
print("<{}>".format(answer))
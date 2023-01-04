n, m = map(int, input().split())
data = list(map(int, input().split()))
queue = [i for i in range(1,n+1)]
counter = 0

while (data) :
    targetIndex = queue.index(data[0])
    if (data[0] == queue[0]) :
        data.pop(0)
        queue.pop(0)
        continue
    elif (targetIndex > len(queue)/2) : queue.insert(0, queue.pop())
    else : queue.append(queue.pop(0))
    counter += 1
    
print(counter)




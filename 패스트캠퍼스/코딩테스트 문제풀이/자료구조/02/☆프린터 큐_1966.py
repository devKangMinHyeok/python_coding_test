test_case = int(input())

for _ in range(test_case):
    n, m = map(int, input().split())
    queue = list(map(int, input().split()))
    queue = [(i, num) for i , num in enumerate(queue)]
    counter = 1
    
    while (queue) :
        if (queue[0][1] == max(queue, key= lambda x : x[1])[1]):
            if (queue[0][0] == m) : break
            else :
                queue.pop(0)
                counter += 1
        else :
            queue.append((queue.pop(0)))
    
    print(counter)
            
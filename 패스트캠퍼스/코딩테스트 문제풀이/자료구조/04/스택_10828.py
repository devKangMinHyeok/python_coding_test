n = int(input())
stack = []
size = 0
answer = []
for _ in range(n):
    data = list(map(str, input().split()))
    com = data[0]
    if (com == "push"): 
        stack.append(data[1])
        size += 1
    elif (com == "top"): 
        if stack : answer.append(stack[-1])
        else : answer.append("-1")
    elif (com == "pop"):
        if stack : 
            answer.append(stack.pop())
            size -= 1
        else : answer.append("-1")
    elif (com == "size"): answer.append(str(size))
    elif (com == "empty"): 
        if stack: answer.append("0")
        else : answer.append("1")
print("\n".join(answer))

n = int(input())

for _ in range(n):
    data = list(input())
    stack1 = []
    stack2 = []
    
    for s in data:
        if (s == '<'):
            if stack1: stack2.append(stack1.pop())
        elif (s == ">"):
            if stack2: stack1.append(stack2.pop())
        elif (s == "-"):
            if stack1: stack1.pop()
            
        else:
            stack1.append(s)
    stack2.reverse()
    result = "".join(stack1 + stack2)
    print(result)
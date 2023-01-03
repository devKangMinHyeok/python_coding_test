n = int(input())
stack = []
sub_list = [i for i in range(n,0,-1)]
last_push = 0
answer = [];
flag = False

for i in range(n):
    if (flag) : break
    target = int(input())
    while (True) :
        if (target < last_push) :
            print("NO")
            flag = True
            break
        elif (target == last_push) :
            answer.append("-")
            stack.pop()
            if (len(stack)): last_push = stack[-1]
            break
        else :
            answer.append("+")
            last_push = sub_list.pop()
            stack.append(last_push)
if (not flag):
    for ans in answer:
        print(ans)
        
    
T = int(input())

def makeOper(array, subArray, max_len):
    if len(subArray) == max_len:
        subArray = subArray[:]
        array.append(subArray)
        return 0
    
    subArray.append("")
    makeOper(array, subArray, max_len)
    subArray.pop()
    
    subArray.append("+")
    makeOper(array, subArray, max_len)
    subArray.pop()
    
    subArray.append("-")
    makeOper(array, subArray, max_len)
    subArray.pop()

for _ in range(T):
    N = int(input())
    answer = []
    data = [i for i in range(1, N+1)]
    operators = []
    makeOper(operators, [], N-1)
    
    for oper in operators:
        ans = []
        for i in range(N-1):
            ans.append(data[i])
            ans.append(oper[i])
        ans.append(data[-1])
        expr = "".join([str(i) for i in ans])
        if eval(expr) == 0:
            answer.append(ans)
    
    for i, ans in enumerate(answer):
        new_ans = ""
        for a in ans:
            if a == "": new_ans += " "
            else: new_ans += str(a)
        answer[i] = new_ans
    
    for ans in answer:
        print(ans)
    print("")

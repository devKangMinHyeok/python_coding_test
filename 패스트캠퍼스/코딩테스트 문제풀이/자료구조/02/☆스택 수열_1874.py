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

"""
복기
- sub_list는 필요가 없다. count int 변수 하나로 컨트롤 할 수 있다.
- last_push도 필요 없다. stack을 잘 업데이트하기만 하면, 배열의 마지막 원소를 가져오면 된다. a[-1]
- while문을 어디서 써야하는지 잘 생각해보자. 그리고 while 조건을 다시 고려해보자
- exit(0)를 사용하면 함수가 아닌 곳에서도 프로그램을 종료할 수 있다. 
"""
        
    
def solution(N, number):
    answer = 0
    DP = [set() for _ in range(9)]
    DP[1] = set(str(N))
    for i in range(2, 9):
        prev_set = DP[i-1]
        for target in prev_set:
            wrapped_target = "(" + target + ")"
            for oper in ["","+","*","-","/"]:
                next1 = target + oper + str(N)
                next2 = wrapped_target + oper + str(N)
                if oper == "": 
                    DP[i].add(next1)
                elif eval(next1) == eval(next2):
                    DP[i].add(next1)
                else:
                    DP[i].add(next1)
                    DP[i].add(next2)
                
                
    for i in range(1,9):
        for expr in DP[i]:
            if int(eval(expr)) == number:
                return i
    return -1


"""
N = 5
N을 1개만 사용
=> 5
N을 2개만 사용
=> 55, 5+5, 5*5, 5-5, 5/5
N을 3개만 사용
=> 
555, 
5+5+5, 5*5+5, 5-5+5, 5/5+5
5+5*5, 5*5*5, ...
"""
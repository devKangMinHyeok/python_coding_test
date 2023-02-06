from collections import deque

s, t = map(int, input().split())

if s == t: 
    print(0)
    exit(0)

if t == 1:
    print("/")
    exit(0)

queue = deque([(s, 0, "")])
visit = set([s])
answer = []

while queue:
    target, level, operator = queue.popleft()
    if target == t:
        answer.append(operator)
        break
    for next_target, next_oper in [(target * target, "*"),(target * 2, "+"), (1, "/")]:
        if next_target < 1 or next_target > 10e9:
            continue
        if next_target not in visit:
            queue.append((next_target, level+1, operator + next_oper))
            visit.add(next_target)

if answer : print("".join(answer))
else: print(-1)
from collections import deque

N, K = map(int, input().split())
num = deque(list(input()))

stack = []
pop_cnt = 0

if N == K:
    print(0)
    exit(0)
    
while num:
    if pop_cnt >= K:
        stack.append(num.popleft())
        continue
    if not stack: stack.append(num.popleft())
    else:
        if stack[-1] >= num[0]:
            stack.append(num.popleft())
        else:
            stack.pop()
            pop_cnt += 1
while pop_cnt < K:
    stack.pop()
    pop_cnt += 1
    
print("".join(stack))
            
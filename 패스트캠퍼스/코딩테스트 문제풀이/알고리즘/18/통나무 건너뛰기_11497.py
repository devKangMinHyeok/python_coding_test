import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    data = list(map(int, input().split()))
    data.sort(reverse=True)
    stack1 = []
    stack2 = []
    
    while data:
        if len(stack1) <= len(stack2):
            stack1.append(data.pop())
        elif len(stack1) > len(stack2):
            stack2.append(data.pop())

    stack2.reverse()
    combine = stack1 + stack2
    max_val = 0
    for i in range(N-1):
        max_val = max(max_val, abs(combine[i] - combine[i+1]))
    print(max_val)
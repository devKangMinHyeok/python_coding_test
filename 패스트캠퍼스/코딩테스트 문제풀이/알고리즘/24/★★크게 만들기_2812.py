from collections import deque

n, k = map(int, input().split())
num = input()
num = deque(list(num))
stack = []
deleted = 0
while num:
    target = num.popleft()
    while stack and target > stack[-1] and deleted < k:
        stack.pop()
        deleted += 1
    stack.append(target)

while stack and deleted < k:
    stack.pop()
    deleted += 1

print("".join(stack))
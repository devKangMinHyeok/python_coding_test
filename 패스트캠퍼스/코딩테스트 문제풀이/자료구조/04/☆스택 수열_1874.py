import sys
input = sys.stdin.readline

n = int(input())
stack = []
answer = []
current = 1

for _ in range(n):
    target = int(input())
    while not stack or stack[-1] < target:
        stack.append(current)
        current += 1
        answer.append("+")
    if stack[-1] == target:
        stack.pop()
        answer.append("-")
    elif stack[-1] > target:
        print("NO")
        exit(0)

print("\n".join(answer))
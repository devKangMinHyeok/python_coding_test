n = int(input())
stack = []

for _ in range(n):
    integer = int(input())
    if (integer == 0 and stack) : stack.pop()
    else : stack.append(integer)

print(sum(stack))

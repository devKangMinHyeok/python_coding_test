n = int(input())
data = list(map(int, input().split()))
stack = []
result = ["-1"] * n

for i, num in enumerate(data):
    if (not stack or stack[-1][1] > num):
        stack.append((i, num))
    else :
        while (stack and stack[-1][1] < num):
            index, _ = stack.pop()
            result[index] = str(num)
        stack.append((i, num))

print(" ".join(result))
        
        
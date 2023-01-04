n = int(input())
data = list(map(int, input().split(" ")))
result = []
for i in range(n-1):
    target = data[i]
    answer = -1
    for j in range(i+1, n):
        if (target < data[j]): 
            answer = data[j]
            break
    result.append(str(answer))
result.append("-1")
print(" ".join(result))
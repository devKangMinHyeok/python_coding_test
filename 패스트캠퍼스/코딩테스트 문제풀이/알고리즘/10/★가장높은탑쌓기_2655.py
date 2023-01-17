n = int(input())
data = [(100000000, -1,-1)]
DP = [(-1,-1)] * (n+1)
for i in range(1,n+1):
    width, height, weight = map(int, input().split())
    data.append((width, height, weight, i))
data.sort(reverse=True)
for i in range(1,len(data)):
    DP[i] = (data[i][1], -1, data[i][3])

for i in range(2,n+1):
    for j in range(1,i):
        if data[j][0] > data[i][0] and data[j][2] > data[i][2]:
            if DP[i][0] < DP[j][0] + data[i][1]:
                DP[i] = (DP[j][0] + data[i][1], j, data[i][3])


max_height = max(DP)
max_index = DP.index(max_height)
counter = 1
stack = []
target = max_index

while DP[target][1] != -1:
    stack.append(DP[target][2])
    counter += 1
    target = DP[target][1]
stack.append(DP[target][2])



print(counter)

for num in stack:
    print(num)
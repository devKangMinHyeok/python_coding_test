import sys
input = sys.stdin.readline

n = int(input())
data = []
answer = 0

for _ in range(n):
    x, y = map(int, input().split())
    data.append((x,y))

data.sort()

prev_x, prev_y = data[0][0], data[0][1]
for i in range(1,len(data)):
    x, y = data[i]
    if prev_y >= x: prev_y = max(y, prev_y)
    else: 
        answer += prev_y - prev_x
        prev_x = x
        prev_y = y

answer += prev_y - prev_x
print(answer)
    

import sys
input = sys.stdin.readline
data = []
n = int(input())
for _ in range(n):
    data.append(int(input()))
    
left = 0
right = 0

max = 0
for num in data:
    if num > max: 
        max = num
        left += 1

max = 0
data.reverse()
for num in data:
    if num > max: 
        max = num
        right += 1
    
print(left)
print(right)
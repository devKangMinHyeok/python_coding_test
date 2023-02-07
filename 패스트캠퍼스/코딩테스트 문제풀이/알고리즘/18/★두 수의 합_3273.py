import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
x = int(input())

data.sort()

start = 0
end = n-1
cnt = 0

while start < end:
    sum = data[start] + data[end]
    if sum > x:
        end -= 1
    elif sum < x:
        start += 1
    else:
        cnt += 1
        start += 1

print(cnt)
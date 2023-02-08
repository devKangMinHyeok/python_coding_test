import sys
input = sys.stdin.readline

n = int(input())
data = []
for _ in range(n):
    data.append(int(input()))

max_val = max(data)
cnt = 0

for i in range(n-1, -1, -1):
    if data[i] == max_val:
        cnt += 1
        max_val -= 1

print(n - cnt)
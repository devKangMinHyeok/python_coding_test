import sys
input = sys.stdin.readline

n = int(input())
data = []
for _ in range(n): data.append(int(input()))

max_val = max(data)
max_index = data.index(max_val)

counter = 1

for i in range(max_index-1,-1,-1):
    if data[i] == max_val-1:
        max_val -= 1
        counter += 1

print(n - counter)
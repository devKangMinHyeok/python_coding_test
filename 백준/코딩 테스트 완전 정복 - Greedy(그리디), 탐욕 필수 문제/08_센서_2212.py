import sys
N = int(input())
K = int(input())
data = list(map(int, input().split()))

if N == 1:
    print(0)
    exit(0)

data.sort()

table = []

for i in range(N-1):
    table.append(data[i+1] - data[i])

table.sort()
for _ in range(K-1):
    table.pop()

print(sum(table))

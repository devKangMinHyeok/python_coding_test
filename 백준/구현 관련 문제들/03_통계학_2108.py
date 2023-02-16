import sys
input = sys.stdin.readline

N = int(input())
data = []
for _ in range(N):
    data.append(int(input()))
data.sort()
print(int(round(sum(data) / N,0)))
print(data[N//2])
table = {}
max_num = 0

for i in data:
    if i in table: table[i] += 1
    else: table[i] = 1
    max_num = max(table[i], max_num)
max_set = []
for i in table:
    if max_num == table[i]:
        max_set.append(i)
max_set.sort()

if len(max_set) > 1: print(max_set[1])
else:print(max_set[0])
print(data[-1] - data[0])
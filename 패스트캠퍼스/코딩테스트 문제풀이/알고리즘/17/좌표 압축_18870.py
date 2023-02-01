import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
data = [(data[i], i) for i in range(n)]
data.sort()
result = []
cnt = 0

for i in range(n-1):
    result.append((cnt, data[i][1]))
    if data[i][0] < data[i+1][0]: cnt += 1

result.append((cnt, data[-1][1]))
result.sort(key = lambda x : x[1])

for i,(num, index) in enumerate(result):
    if i < n-1: print(num, end=" ")
    else: print(num)
    
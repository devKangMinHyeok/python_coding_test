"""
data = [(25, 3, 4), (16, 2, 5), (9, 2, 3), (4, 4, 6), (1, 5, 2)]

    0     25    16    9     4    1
0   0     0     0     0     0    0
1   0     3     0     0     0    0
2   0     3     2     0     0    0
3   0     3     2     5     0    0
4   0     3     2     5     4    0
5   0     3     2     5,0   4    10,2   
"""

import sys
input = sys.stdin.readline

n = int(input())
data = [(100000,100000,100000)]

for i in range(n):
    width, height, weight = map(int, input().split())
    data.append((width, height, weight, i+1))

data.sort(key = lambda x : (x[0], x[2]), reverse = True)

dp = [(0,0,0) for _ in range(n+1)]

for i in range(1,len(data)):
    dp[i] = (data[i][1], 0, data[i][3])

for i in range(1, len(data)):
    width, height, weight, index = data[i]
    for j in range(1,i):
        if weight < data[j][2]:
            if dp[i][0] < data[i][1] + dp[j][0]:
                dp[i] = (data[i][1] + dp[j][0], j, index)


max_height = max(dp, key=lambda x : x[0])
target_index = dp.index(max_height)
count = 1
answer = []
while dp[target_index][1]:
    answer.append(dp[target_index][2])
    target_index = dp[target_index][1]
    count += 1

answer.append(dp[target_index][2])
print(count)
for num in answer:
    print(num)


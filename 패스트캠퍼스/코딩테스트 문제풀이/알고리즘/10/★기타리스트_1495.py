import sys
input = sys.stdin.readline

n, start, max_num = map(int, input().split())
data = list(map(int, input().split()))

able = [False] * (max_num + 1)
able[start] = True

for num in data:
    new_able = [False] * (max_num + 1)
    for i in range(len(able)):
        if able[i]:
            if i - num >= 0: new_able[i-num] = True
            if i + num <= max_num: new_able[i+num] = True
    able = new_able

answer = -1
for i in range(len(able)):
    if able[i]: answer = i

print(answer)
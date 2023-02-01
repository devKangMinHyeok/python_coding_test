import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
x = int(input())

count = 0
targets = set()

for i in range(n):
    target = x - data[i]
    targets.add(target)

for i in range(n):
    if data[i] in targets: count += 1

print(count // 2)

"""
투포인터 풀이도 가능
"""
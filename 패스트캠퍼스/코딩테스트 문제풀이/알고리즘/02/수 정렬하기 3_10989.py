import sys
input = sys.stdin.readline

n = int(input())
table = {}

for _ in range(n):
    num = int(input())
    if num in table: table[num] += 1
    else: table[num] = 1
table = sorted(table.items())
for key, num in table:
    for _ in range(num):
        print(key)
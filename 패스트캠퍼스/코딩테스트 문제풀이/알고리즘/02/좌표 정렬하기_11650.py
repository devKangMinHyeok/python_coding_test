import sys
input = sys.stdin.readline

n = int(input())
table = []

for _ in range(n):
    x, y = map(int, input().split())
    table.append((x,y))

table = sorted(table, key=lambda item : (item[0], item[1]))
for i in range(n):
    x, y = table[i]
    print(x, y)
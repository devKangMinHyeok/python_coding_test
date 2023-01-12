import sys
input = sys.stdin.readline

n = int(input())
table = []

for i in range(n):
    age, name = map(str, input().split())
    age = int(age)
    table.append((age,name))

table = sorted(table, key = lambda item : (item[0]))

for data in table:
    print(data[0], data[1])
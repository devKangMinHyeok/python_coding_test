import sys
input = sys.stdin.readline

n = int(input())
array = []
for _ in range(n):
    age, name = map(str, input().split())
    age = int(age)
    array.append((age, name))
array = sorted(array, key=lambda ele : ele[0])
for data in array:
    print(data[0], data[1])
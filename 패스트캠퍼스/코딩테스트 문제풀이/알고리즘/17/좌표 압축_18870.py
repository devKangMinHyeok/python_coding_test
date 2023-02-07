import sys
input = sys.stdin.readline

N = int(input())
data = list(map(int, input().split()))

new_data = list(set(data))
new_data.sort()

table = {}
for i, num in enumerate(new_data):
    table[num] = i

for num in data:
    print(table[num], end=" ")

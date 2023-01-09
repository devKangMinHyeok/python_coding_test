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
    
"""
dictionary로 table을 구현하면 같은 age일때 먼저들어온 것이 무엇인지 바로 알 수 없다.
"""
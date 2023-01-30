import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
data.sort()

time = 1
comp = []

while data:
    comp.append(time + data.pop() + 1)
    time += 1

print(max(comp))


"""
    4 3 3 2
1   - 
2   4 - 
3   3 3 - 
4   2 2 3 -
5   1 1 2 2
6   0 0 1 1
7   0 0 0 0
"""
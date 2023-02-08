import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

def dfs(path):
    global answer
    Sum = sum(path)
    if Sum == n:
        answer += 1
        return 
    elif Sum > n:
        return
    for next_num in [1,2,3]:
        path.append(next_num)
        dfs(path)
        path.pop()
    

for _ in range(T):
    n = int(input())
    answer = 0
    dfs([])
    print(answer)
    
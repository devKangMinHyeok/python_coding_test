import sys
from collections import deque
input = sys.stdin.readline

def parser(paths):
    if paths == "":
        return 100
    else: 
        return int(paths)

N = int(input())
M = int(input())
excpt_button = []
start = 100
answer = abs(100 - N)

if M: excpt_button = set(list(map(int,input().split())))

for i in range(0, 1000000):
    able = True
    for btn in str(i):
        if int(btn) in excpt_button:
            able = False
            break
    if able:
        new_ans = abs(i - N) + len(str(i))
        answer = min(answer, new_ans)
        
print(answer)
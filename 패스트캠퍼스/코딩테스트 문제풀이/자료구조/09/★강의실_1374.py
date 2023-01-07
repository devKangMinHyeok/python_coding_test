import sys
input = sys.stdin.readline

n = int(input())
lecs = []
time = 0
count = 0

for _ in range(n):
    num, start, end = map(int, input().split())
    lecs.append((start, end))

while lecs :
    is_full = True
    
    for lec in lecs:
        if lec[0] >= time: 
            is_full = False 
            break
    if is_full : 
        time = 0
        count += 1
    
    min_num = 10000000000
    target_i = -1
    
    for i, lec in enumerate(lecs):
        if min_num > lec[0] and time < lec[0]:
            min_num = lec[0]
            target_i = i
    
    _, time = lecs[target_i]
    lecs[target_i]
    
count += 1

print(count)
    
    

    
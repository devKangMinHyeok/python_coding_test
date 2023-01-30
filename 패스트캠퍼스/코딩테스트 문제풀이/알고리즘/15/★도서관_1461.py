import sys
input = sys.stdin.readline

n, m = map(int, input().split())
place = list(map(int, input().split()))
n_place = []
p_place = []

for p in place:
    if p < 0:
        n_place.append(-p)
    else:
        p_place.append(p)

n_place.sort()
p_place.sort()

max_val = 0
if n_place: max_val = max(n_place)
if p_place: max_val = max(max_val, max(p_place))

answer = 0

while p_place:
    for i in range(m):
        if i == 0: 
            answer += p_place.pop() * 2
        elif p_place:
            p_place.pop()

while n_place:
    for i in range(m):
        if i == 0: 
            answer += n_place.pop() * 2
        elif n_place:
            n_place.pop()

answer -= max_val

print(answer)
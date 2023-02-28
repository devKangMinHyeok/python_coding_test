import sys
input = sys.stdin.readline

N, L = map(int, input().split())
lines = []

for _ in range(N):
    a, b = map(int, input().split())
    lines.append((a,b-1))

lines.sort()
start = -1
end = -1
new_lines = []

for a, b in lines:
    if end >= a:
        end = max(end, b)
    else:
        new_lines.append((start, end))
        start = a
        end = b
new_lines.append((start, end))
lines = new_lines[1:]

answer = 0
null_end = -1


for a,b in lines:
    if null_end < a:
        null_end = a-1
    length = b-null_end
    if length % L == 0:
        answer += length // L
        null_end = b
    else:
        answer += length // L + 1
        null_end += (length // L + 1) * L
        
print(answer)
        
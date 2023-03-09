import sys
input = sys.stdin.readline

N, C = map(int, input().split())
positions = []
for _ in range(N):
    positions.append(int(input()))
positions = list(set(positions))
positions.sort()

def check(length):
    cnt = 1
    prev = positions[0]
    for i in range(1, len(positions)):
        pos = positions[i]
        if pos - prev >= length:
            prev = pos
            cnt += 1
    return cnt

low = 0
high = positions[-1] - positions[0]
ans = -1

while low <= high:
    mid = (low + high) // 2
    if check(mid) >= C:
        low = mid + 1
        ans = mid
    else:
        high = mid - 1

print(ans)
import sys
input = sys.stdin.readline

N, M, L = map(int, input().split())
slices = []
T = []
for _ in range(M): slices.append(int(input()))
for _ in range(N): T.append(int(input()))
slices.sort()

def able(pivot, number):
    pieces = []
    prev = 0
    cnt = 0
    for slice in slices:
        if cnt >= number: break
        length = slice - prev
        if length >= pivot:
            prev = slice
            pieces.append(length)
            cnt += 1
    pieces.append(L - prev)
    if min(pieces) >= pivot and cnt == number: return True
    else: return False
            

for number in T:
    low = 1
    high = max(slices)
    ans = -1
    while low <= high:
        mid = (low + high) // 2
        if able(mid, number):
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
    print(ans)
    
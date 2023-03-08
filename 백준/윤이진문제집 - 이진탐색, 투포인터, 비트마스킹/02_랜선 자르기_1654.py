import sys
input = sys.stdin.readline

K , N = map(int, input().split())
lines = []
for _ in range(K):
    lines.append(int(input()))

def cutter(length):
    acc = 0
    for line in lines:
        acc += line // length
    return acc

def binary_search():
    low = 1
    high = max(lines)
    ans = -1
    while low <= high:
        mid = (low + high) // 2
        if cutter(mid) >= N:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
    return ans

print(binary_search())
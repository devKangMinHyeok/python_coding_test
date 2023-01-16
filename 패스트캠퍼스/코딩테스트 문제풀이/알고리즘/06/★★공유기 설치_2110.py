import sys
input = sys.stdin.readline

n, c = map(int, input().split())
arr = []

for _ in range(n):
    arr.append(int(input()))

arr.sort()

low = 1
high = arr[-1] - arr[0]
answer = 0

def find_w(gap):
    count = 1
    current = arr[0]
    for i in range(1,len(arr)):
        if current + gap <= arr[i]:
            count += 1
            current = arr[i]
    return count

while low <= high:
    mid = (low + high) // 2
    if find_w(mid) >= c:
        answer = mid
        low = mid + 1
    else:
        high = mid - 1

print(answer)
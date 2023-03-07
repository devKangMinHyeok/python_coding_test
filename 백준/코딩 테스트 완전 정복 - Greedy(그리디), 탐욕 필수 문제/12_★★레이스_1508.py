import sys
from heapq import heappush, heappop
input = sys.stdin.readline

N, M, K = map(int, input().split())
tracks = list(map(int, input().split()))

def able(pivot):
    prev = tracks[0]
    count = 1
    for i in range(1,K):
        if prev + pivot <= tracks[i]:
            count += 1
            prev = tracks[i]
    if M <= count: return True
    else: return False

def binary_search():
    low = 0
    high = N
    ans = 0
    while low <= high:
        mid = (low + high) // 2
        if able(mid):
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
    return ans

max_dist = binary_search()
prev = tracks[0]
answer = "1"
counter = 1

for i in range(1, K):
    if counter < M and prev + max_dist <= tracks[i]:
        counter += 1
        answer += "1"
        prev = tracks[i]
    else:
        answer += "0"
print(answer)
            
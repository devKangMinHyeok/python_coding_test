import sys
from heapq import heappush, heappop
input = sys.stdin.readline

N, M, K = map(int, input().split())
tracks = list(map(int, input().split()))
tracks.sort()

table = []

for i in range(K-1):
    heappush(table, (tracks[i+1] - tracks[i], i))

for _ in range(K-M):
    heappop(table)

print(table)
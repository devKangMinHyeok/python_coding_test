import sys
from itertools import combinations
input = sys.stdin.readline

N, S = map(int, input().split())
data = list(map(int, input().split()))
answer = 0

for i in range(1,N+1):
    result = combinations(data, i)
    for res in result:
        if sum(res) == S:
            answer += 1

print(answer)
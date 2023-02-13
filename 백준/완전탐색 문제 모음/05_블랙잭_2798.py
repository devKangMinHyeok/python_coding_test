import sys
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().split())
cards = list(map(int, input().split()))
result = combinations(cards, 3)
max_score = 0

for res in result:
    if sum(res) <= M: max_score = max(max_score, sum(res))

print(max_score)
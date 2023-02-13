import sys
from itertools import combinations
input = sys.stdin.readline

def check(target):
    moem = 0
    for character in target:
        if character in ['a','e','i','o','u']:
            moem += 1
    if moem < 1: return False
    if len(target) - moem < 2: return False
    return True

L, C = map(int, input().split())
data = list(map(str, input().split()))
data.sort()

result = combinations(data, L)

for res in result:
    res = "".join(map(str, res))
    if check(res):
        print(res)
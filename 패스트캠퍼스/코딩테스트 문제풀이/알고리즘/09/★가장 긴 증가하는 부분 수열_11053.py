"""
하나의 숫자를 기준으로, 그것을 마지막 원소라고 생각했을 때 최대 길이 구하기
"""

import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
DP = [1] * n

for i in range(1,n):
    for j in range(0,i+1):
        if data[i] > data[j]: DP[i] = max(DP[j]+1, DP[i])

print(max(DP))
"""
하나의 숫자를 기준으로, 그것을 마지막 원소라고 생각했을 때 최대 길이 구하기
"""

import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

dp = [1 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if data[j] < data[i]:
            dp[i] = max(dp[i], dp[j]+1)
        
print(max(dp))
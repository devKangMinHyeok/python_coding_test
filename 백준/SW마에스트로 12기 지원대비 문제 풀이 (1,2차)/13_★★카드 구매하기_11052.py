import sys
N = int(input())
cards = [0] * (N+1)
c_input = list(map(int, input().split()))
for i in range(1, N+1):
    cards[i] = c_input[i-1]
    
DP = [0] * (N+1)
for i in range(1, N+1): # 최대 카드 수
    for j in range(1, i+1):
        DP[i] = max(DP[i], DP[i-j] + cards[j])

print(DP[N])


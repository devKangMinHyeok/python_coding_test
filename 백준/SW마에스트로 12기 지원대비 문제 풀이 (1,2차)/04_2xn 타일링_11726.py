n = int(input())

DP = [-1] * n
DP[0] = 1
if n > 1:
    DP[1] = 2

for i in range(2,n):
    DP[i] = (DP[i-1] + DP[i-2]) % 10007

print(DP[n-1])

"""
  0 A C A Y K P
0 0 0 0 0 0 0 0
C 0 0 1 1 1 1 1
A 0 [1] 1 2 2 2 2
P 0 1 1 2 2 2 3
C 0 1 [2] 2 2 2 3
A 0 1 2 [3] 3 3 3
K 0 1 2 3 3 [4] 4

"""

a = input()
b = input()

dp = [[0 for _ in range(len(a)+1)] for __ in range(len(b)+1)]

for i in range(1, len(b)+1):
  for j in range(1, len(a)+1):
    if b[i-1] == a[j-1]: dp[i][j] = dp[i-1][j-1] + 1
    else: dp[i][j] = max(dp[i][j-1], dp[i-1][j])

print(dp[-1][-1])
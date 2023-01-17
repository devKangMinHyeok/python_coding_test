"""
  A C A Y K P
C 0 1 1 1 1 1
A 1 1 2 2 2 2
P 1 1 2 2 2 3
C 1 2 2 2 2 3
A 2 2 3 3 3 3 
K 2 2 3 3 4 4


"""

a = input()
b = input()

DP = [[0] * (len(a)+1) for _ in range(len(b)+1)]

for i in range(1,len(b)+1):
    for j in range(1,len(a)+1):
        if b[i-1] == a[j-1]: DP[i][j] = DP[i-1][j-1] + 1
        else: DP[i][j] = max(DP[i-1][j], DP[i][j-1])

print(DP[len(b)][len(a)])
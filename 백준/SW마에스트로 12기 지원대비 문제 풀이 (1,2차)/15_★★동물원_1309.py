N = int(input())

DP = [[0] * (N+1) for _ in range(3)]
DP[0][1], DP[1][1], DP[2][1] = 1, 1, 1


for i in range(2,N+1):
    DP[0][i] = (DP[1][i-1] + DP[2][i-1] + DP[0][i-1]) % 9901
    DP[1][i] = (DP[0][i-1] + DP[2][i-1]) % 9901
    DP[2][i] = (DP[0][i-1] + DP[1][i-1]) % 9901
    
print(sum([DP[0][N], DP[1][N], DP[2][N]]) % 9901)


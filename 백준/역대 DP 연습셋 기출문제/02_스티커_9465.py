import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    DP = []
    for __ in range(2):
        DP.append(list(map(int , input().split())))
    
    if n == 1:
        print(max(DP[0][0], DP[1][0]))
        continue
    DP[0][1] += DP[1][0]
    DP[1][1] += DP[0][0]
    
    for i in range(2, n):
        DP[0][i] += max(DP[1][i-1], DP[0][i-2], DP[1][i-2])
        DP[1][i] += max(DP[0][i-1], DP[0][i-2], DP[1][i-2])
        
    print(max(max(DP[0]), max(DP[1])))
    
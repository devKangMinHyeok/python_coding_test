import sys
input = sys.stdin.readline

DP = [1,1,1,2,2,3,4,5,7,9]

T = int(input())
for _ in range(T):
    N = int(input())
    for i in range(3, N+1):
        if len(DP) == i:
            DP.append(0)
        DP[i] = DP[i-2] + DP[i-3]
    print(DP[N-1])
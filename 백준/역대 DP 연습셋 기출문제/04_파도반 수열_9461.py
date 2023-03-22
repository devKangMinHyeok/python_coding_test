import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    
    if N <= 3: 
        print(1)
        continue
    
    DP = [0] * (N+1)
    DP[1] = 1
    DP[2] = 1
    
    DP[3] = 1
    
    for i in range(4, N+1):
        DP[i] = DP[i-2] + DP[i-3]
        
    print(DP[N])
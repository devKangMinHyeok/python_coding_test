import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    data = list(map(int, input().split()))
    table = [-1] * N
    max_val = -1
    
    for i in range(N-1, -1, -1):
        max_val = max(max_val, data[i])
        table[i] = max_val
    
    sum = 0
    for i in range(N):
        sum += table[i] - data[i]
    print(sum)
    
    
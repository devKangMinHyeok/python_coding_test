import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    stocks = list(map(int, input().split()))
    table = [0] * n
    max_val = 0
    for i in range(n-1, -1, -1):
        max_val = max(max_val, stocks[i])
        table[i] = max_val
    for i in range(n):
        table[i] = table[i] - stocks[i]
    print(sum(table))
    
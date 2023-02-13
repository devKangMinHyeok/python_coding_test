import sys
input = sys.stdin.readline

N = int(input())
data = list(map(int, input().split()))

DP = [1] * N 
for i in range(1, N):
    for j in range(i):
        if data[j] < data[i]:
            DP[i] = max(DP[i], DP[j] + 1)
print(max(DP))


"""
    10 20 10 30 20 50
0   1  1  1  1  1  1
1   1  2  1  1  1  1
2   1  2  1  1  1  1
3   1  2  1  3  1  1
4   1  2  1  3  2  1
5   1  2  1  3  2  4


"""
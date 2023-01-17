import sys
input = sys.stdin.readline

n, start, max_v = map(int, input().split())
V = list(map(int, input().split()))
DP = [False] * (max_v + 1)
DP[start] = True

for vol in V:
    new_DP = [False] * (max_v + 1)
    for i in range(len(DP)):
        if DP[i]:
            if i-vol >= 0: new_DP[i-vol] = True
            if i+vol <= max_v: new_DP[i+vol] = True
    DP = new_DP

for i in range(len(DP)-1, -1, -1):
    if DP[i]: 
        print(i)
        exit(0)
print(-1)
            


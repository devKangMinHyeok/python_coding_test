import sys
input = sys.stdin.readline

def dfs(prev, lp, hp):
    global max_happy
    for i in range(prev+1, N):
        if lp - loss[i] > 0: 
            max_happy = max(max_happy, hp+happy[i])
            dfs(i, lp-loss[i], hp+happy[i])
        else:
            max_happy = max(max_happy, hp)

N = int(input())
loss = list(map(int, input().split()))
happy = list(map(int, input().split()))
max_happy = 0

dfs(-1, 100, 0)
print(max_happy)
import sys
input = sys.stdin.readline

n = int(input())
rank = []
for i in range(n):
    rank.append(int(input()))
rank.sort()
answer = 0
for i in range(len(rank)):
    answer += abs(i+1 - rank[i])
print(answer)
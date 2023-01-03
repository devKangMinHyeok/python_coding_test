n = int(input())
A = list(map(int, input().split()))
m = int(input())
M = list(map(int, input().split()))

map = {}

for i in range(n):
    if not(A[i] in map): map[A[i]] = True

for i in range(m):
    if M[i] in map: print(1)
    else: print(0)
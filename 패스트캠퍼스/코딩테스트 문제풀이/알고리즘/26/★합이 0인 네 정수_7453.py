import sys
input = sys.stdin.readline

n = int(input())

A = []
B = []
C = []
D = []

for _ in range(n):
    a, b, c, d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

counter = {}
answer = 0

for i in range(n):
    for j in range(n):
        sum = A[i] + B[j]
        if sum in counter: counter[sum] += 1
        else: counter[sum] = 1

for i in range(n):
    for j in range(n):
        sum = C[i] + D[j]
        if -sum in counter: answer += counter[-sum]

print(answer)


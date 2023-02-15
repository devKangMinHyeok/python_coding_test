import sys
input = sys.stdin.readline

def is_prime(n):
    if n == 1 or n == 0: return False
    if n == 2: return True
    for i in range(2, n):
        if i * i > n: break
        if n % i == 0: return False
    return True

def solve(a, p, P):
    if p == 1: return a % P
    if p == 2: return (a * a) % P
    temp = solve(a, p//2, P)
    temp = (temp * temp) % P
    if p % 2:
        return (temp * a) % P
    else:
        return (temp) % P

while True:
    p, a = map(int, input().split())
    if p == 0 and a == 0: break
    if is_prime(p): print("no")
    elif solve(a,p,p) == a % p: print("yes")
    else: print("no")
    
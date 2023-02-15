A, B, C = map(int, input().split())

def solve(a, b):
    if b == 1:
        return a % C
    if b == 2:
        return ((a % C) * (a % C)) % C
    target = solve(a, b//2)
    if b % 2 == 0:
        return (target * target) % C
    else:
        return (target * target * a) % C

result = solve(A,B)
print(result)
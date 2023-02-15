N, R = map(int, input().split())
DEVIDER = 1000000007 

def solve(n, r):
    if n == 0: return 0
    if r == 0: return 1
    if n > 1 and r > 1: 
        return solve(n-1,r-1) + solve(n-1,r)
    
    top = 1
    for i in range(n, n - r, -1):
        top = (top * i) 
    bottom = 1
    for i in range(r, 1, -1):
        bottom = (bottom * i) 
    return (top // bottom) % DEVIDER
        

print(solve(N, R))
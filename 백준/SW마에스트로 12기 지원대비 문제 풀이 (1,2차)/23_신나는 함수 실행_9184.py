
def recursion(a, b, c):
    if (a, b, c) in DP: return DP[(a,b,c)]
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return recursion(20, 20, 20)
    if a < b and b < c:
        DP[(a,b,c)] = recursion(a, b, c-1) + recursion(a, b-1, c-1) - recursion(a, b-1, c)
        return DP[(a,b,c)]
    else:
        DP[(a,b,c)] = recursion(a-1, b, c) + recursion(a-1, b-1, c) + recursion(a-1, b, c-1) - recursion(a-1, b-1, c-1)
        return DP[(a,b,c)]
    

DP = {}

while True:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1: break
    print("w({0}, {1}, {2}) = {3}".format(a, b, c, recursion(a,b,c)))
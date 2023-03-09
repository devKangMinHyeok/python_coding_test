import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
beers = []
for _ in range(K):
    v, c = map(int, input().split())
    beers.append((v,c))
beers.sort(key = lambda x : -x[0], )

def able(level):
    selected = []
    for v, c in beers:
        if c <= level: selected.append(v)
    selected.sort(reverse=True)
    acc = 0
    for i, s in enumerate(selected):
        if i + 1 > N: break
        acc += s
    if acc >= M and len(selected) >= N:
        return True
    else:
        return False
    

def binary_search():
    low = 0
    high = pow(2,31)
    ans = -1
    
    while low <= high:
        mid = (low + high) // 2
        if able(mid):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
            
    return ans
ans = binary_search()
print(ans)
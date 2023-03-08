import sys
input = sys.stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))

def cutter(height):
    acc = 0
    for tree in trees:
        if tree > height:
            acc += tree - height
    return acc

def binary_search():
    low = 0
    high = max(trees)
    ans = -1
    
    while low <= high:
        mid = (low + high) // 2
        if M <= cutter(mid):
            ans = mid
            low = mid +1
        else:
            high = mid - 1
    return ans

print(binary_search())
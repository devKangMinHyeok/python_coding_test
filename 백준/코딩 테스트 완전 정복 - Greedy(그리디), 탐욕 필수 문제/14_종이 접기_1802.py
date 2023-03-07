import sys

T = int(input())

def check(folded):
    n = len(folded)
    if n == 1: return True
    pivot = n // 2
    for i in range(1,pivot+1):
        if folded[pivot - i] != folded[pivot + i]:
            continue
        else:
            return False
    return True
            
def recursion(target):
    if len(target) == 1:
        return True
    if check(target):
        return recursion(target[len(target)//2 + 1:])
    return False

for _ in range(T):
    folded = input()
    if recursion(folded): print("YES")
    else: print("NO")
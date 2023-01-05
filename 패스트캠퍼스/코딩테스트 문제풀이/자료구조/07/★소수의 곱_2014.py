from itertools import combinations
from heapq import heappush, nsmallest

k, n = map(int, input().split())
org_primes = list(map(int, input().split()))
primes = [i for i in org_primes]
heap = []
count = 0
while len(heap) <= n or min(primes) < nsmallest(n,heap)[-1]:
    if (count) : primes = [num ** (count+1) for num in org_primes]
    count += 1
    print(primes)
    combi = []
    for i in range(1,k+1):
        combi += list(combinations(primes,i))
    for comb in combi:
        result = 1
        for num in comb:
            result *= num
        heappush(heap, result)
    

print(nsmallest(n,heap))
print(nsmallest(n,heap)[-1])
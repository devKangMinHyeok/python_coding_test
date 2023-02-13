N = int(input())

def is_prime(n):
    if n in primes and primes[n]: return True
    if n == 1: 
        return False
    for i in range(2,n):
        if i*i > n: break
        if n % i == 0: 
            return False
    primes[n] = True
    return True

primes = {}

def dfs(x):
    if len(str(x)) == N and is_prime(x):
        print(x)
        return
    for i in range(0,10):
        target = str(x) + str(i)
        if not is_prime(int(target)): continue
        else:
            dfs(int(target))

dfs(2)
dfs(3)
dfs(5)
dfs(7)
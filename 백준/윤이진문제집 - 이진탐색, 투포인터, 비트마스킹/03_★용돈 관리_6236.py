import sys
input = sys.stdin.readline

N, M = map(int, input().split())
moneys = []
for _ in range(N):
    moneys.append(int(input()))

def able(k):
    account = 0
    cnt = 0
    for money in moneys:
        if account < money:
            account = k
            cnt += 1
            if account >= money:
                account -= money
            else:
                return False
        else:
            account -= money
    return cnt <= M

def binary_search():
    low = 0
    high = sum(moneys)
    ans = -1
    while low <= high:
        mid = (low + high) // 2
        if able(mid):
            high = mid - 1
            ans = mid
        else:
            low = mid + 1
    return ans

answer = binary_search()
print(answer)
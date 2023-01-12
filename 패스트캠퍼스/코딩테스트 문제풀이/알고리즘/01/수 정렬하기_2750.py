import sys
input = sys.stdin.readline

n = int(input())
data = []
for _ in range(n):
    data.append(int(input()))

data.sort()
for num in data:
    print(num)

## 선택 정렬로도 풀어보기
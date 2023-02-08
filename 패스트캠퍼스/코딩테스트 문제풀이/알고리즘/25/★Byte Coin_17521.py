n, W = map(int, input().split())
data = []
for _ in range(n):
    s = int(input())
    data.append(s)

for i in range(n-1):
    if data[i] < data[i+1]:
        coin = W // data[i]
        W = W % data[i]
        W += data[i+1] * coin

print(W)
      
          
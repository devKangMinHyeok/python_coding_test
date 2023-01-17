n = int(input())

if n == 1: 
    print(1)
    exit(0)

a = 1 # 1
b = 2 # 00 11

for i in range(3, n+1):
    a, b = b, (a+b) % 15746

print(b)
     
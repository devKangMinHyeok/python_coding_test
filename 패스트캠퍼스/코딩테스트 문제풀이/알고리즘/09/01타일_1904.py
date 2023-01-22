n = int(input())

a = 1
b = 2

if n == 1: 
    print(a)
    exit(0)
elif n == 2:
    print(b)
    exit(0)

for i in range(3,n+1):
    a, b = b, (a + b) % 15746

print(b)
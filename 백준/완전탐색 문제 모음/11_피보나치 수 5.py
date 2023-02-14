n = int(input())
fibo = [-1] * (n+1)
if n == 0: 
    print(0)
    exit(0)
fibo[0], fibo[1] = 0, 1
for i in range(2,n+1):
    fibo[i] = fibo[i-1] + fibo[i-2]
print(fibo[n])

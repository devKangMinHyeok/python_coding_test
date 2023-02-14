N = int(input())

for i in range(1,N):
    Sum = i
    for j in range(len(str(i))):
        target = int(str(i)[j])
        Sum += target
    if N == Sum:
        print(i)
        exit(0)
print(0)
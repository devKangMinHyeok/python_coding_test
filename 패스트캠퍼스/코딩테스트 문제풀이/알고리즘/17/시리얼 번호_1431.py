n = int(input())
serials = []
for _ in range(n):
    serials.append(input())
for i in range(n):
    sum = 0
    for j in range(len(serials[i])):
        if '1' <= serials[i][j] and serials[i][j] <= '9':
            sum += int(serials[i][j])
    serials[i] = (serials[i], sum)

serials.sort(key = lambda x : (len(x[0]), x[1], x[0]))
for i in range(n):
    print(serials[i][0])
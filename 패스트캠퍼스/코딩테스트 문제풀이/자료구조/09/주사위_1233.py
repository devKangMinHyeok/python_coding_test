s1, s2, s3 = map(int, input().split())

table = {}

for i in range(1,s1+1):
    for j in range(1, s2+1):
        for k in range(1, s3+1):
            sum = i + j + k
            if sum not in table: table[sum] = 1
            else: table[sum] += 1

print(max(table, key= lambda x: table[x]))
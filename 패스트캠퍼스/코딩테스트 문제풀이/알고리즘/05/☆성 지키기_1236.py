n , m = map(int, input().split())
data = []
answer = 0

for _ in range(n):
    data.append([i for i in input()])
for i in range(n):
    for j in range(m):
        row_valid = False
        col_valid = False
        if 'X' in data[i]: row_valid = True
        for k in range(n):
            if data[k][j] == 'X': col_valid = True
        if not row_valid and not col_valid: 
            data[i][j] = 'X'
            answer += 1
for i in range(n):
    for j in range(m):
        row_valid = False
        col_valid = False
        if 'X' in data[i]: row_valid = True
        for k in range(n):
            if data[k][j] == 'X': col_valid = True
        if not row_valid or not col_valid:
            data[i][j] = 'X'
            answer += 1

print(answer)
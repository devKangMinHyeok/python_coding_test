n, m = map(int, input().split())

tower = []

for _ in range(n):
    tower.append(list(input()))

row_empty = 0
col_empty = 0

for i in range(n):
    if 'X' not in tower[i]:
        row_empty += 1

for j in range(m):
    check = False
    for i in range(n):
        if tower[i][j] == 'X': check = True
    if not check: 
        col_empty += 1

print(max(row_empty, col_empty)) 
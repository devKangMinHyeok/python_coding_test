n = int(input())

def check(cur_row):
    for i in range(cur_row):
        if row[i] == row[cur_row]: return False
        if abs(row[i] - row[cur_row]) == cur_row - i: return False
    return True

def dfs(cur_row):
    global answer
    if cur_row == n:
        answer += 1
        return
    for i in range(n):
        row[cur_row] = i
        if check(cur_row):
            dfs(cur_row + 1)

answer = 0
row = [0] * n
dfs(0)
print(answer)
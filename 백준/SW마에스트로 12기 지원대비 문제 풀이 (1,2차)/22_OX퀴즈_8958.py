import sys
input = sys.stdin.readline

def make_table(arr):
    table = []
    cnt = 0
    for ox in arr:
        if ox == "O":
            cnt += 1
        else:
            table.append(cnt)
            cnt = 0
    table.append(cnt)
    return table

def make_sum(n):
    return (n*(n+1))//2

n = int(input())
for _ in range(n):
    arr = list(input())
    table = make_table(arr)
    for i, num in enumerate(table):
        table[i] = make_sum(num)
    print(sum(table))

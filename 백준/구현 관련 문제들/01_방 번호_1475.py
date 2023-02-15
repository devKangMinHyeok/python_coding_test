N = int(input())

table = [len(str(N))] * 10

for s in str(N):
    s_int = int(s)
    if s_int == 9 or s_int == 6:
        if table[6] <= table[9]:
            table[9] -= 1
        else:
            table[6] -= 1
    else:
        table[s_int] -= 1

print(len(str(N)) - min(table))
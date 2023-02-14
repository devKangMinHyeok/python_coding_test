
N = int(input())
table = [3]

while table[-1] < N:
    table.append(table[-1] * 2 + len(table) + 3)

def find_index(n):
    if n <= 3:
        return 0
    for i in range(len(table)):
        if n == table[i]:
            return i
        if n > table[i] and n < table[i+1]:
            return i+1

def solve(n):
    if n <= 3:
        if n == 1: print("m")
        else: print("o")
        return 
    k = find_index(n)
    if table[k-1]+1 == n:
        print("m") 
        return
    elif table[k-1]+1 < n and n <= table[k-1] + k+3:
        print("o")
        return
    else:
        solve(n - (table[k-1] + k+3)) # 10 - (3 + 4) = 3

solve(N)

"""
S(0) = "m o o" => 3
1
S(1) = "m o o m o o o m o o" => 3 + 4 + 3 = 10
1 4 8
S(2) = "m o o m o o o m o o m o o o o m o o m o o o m o o" => 10 + 5 + 10 = 25
1 4 8 11 16 19 23
"""
import sys
input = sys.stdin.readline

n = int(input())
tree = []
for _ in range(n):
    row = list(map(int, input().split()))
    tree.append(row)
    
for i in range(1, n):
    for j in range(i+1):
        left = -1
        right = -1
        if j != 0: left = tree[i-1][j-1]
        if i != j: right = tree[i-1][j]
        tree[i][j] = max(left, right) + tree[i][j]

print(max(tree[n-1]))
    
"""
     0 1 2 3 4
0    7
1    3 8
2    8 1 0
3    2 7 4 4
4    4 5 2 6 5

"""
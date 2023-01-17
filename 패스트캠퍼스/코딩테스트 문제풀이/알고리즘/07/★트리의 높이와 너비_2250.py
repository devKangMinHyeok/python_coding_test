import sys
input = sys.stdin.readline

class Node :
    def __init__ (self, value, left, right):
        self.value = value
        self.left = left
        self.right = right
        self.order = -1
        self.level = -1

n = int(input())
ordering = 1
tree = {}
max_level = 0

for _ in range(n):
    v, l, r = map(int, input().split())
    tree[v] = Node(v, l, r)

def inOrder (root):
    global ordering
    if root.left != -1: inOrder(tree[root.left])
    root.order = ordering
    ordering += 1
    if root.right != -1: inOrder(tree[root.right])

def find_root(tree, n):
    check = [False] * (n+1)
    for value in tree:
        node = tree[value]
        if node.left != -1: check[node.left] = True
        if node.right != -1: check[node.right] = True
    for i in range(1,n+1):
        if not check[i]:
            return i

def leveling(root, level):
    global max_level
    max_level = max(level, max_level)
    root.level = level
    if root.left != -1: leveling(tree[root.left], level+1)
    if root.right != -1: leveling(tree[root.right], level+1)

root = find_root(tree, n)
inOrder(tree[root])
leveling(tree[root], 1)

width = [[] for _ in range(max_level+1)]

for value in tree:
    node = tree[value]
    width[node.level].append(node.order)

for i, level_ws in enumerate(width):
    if level_ws: width[i] = max(level_ws) - min(level_ws) + 1
    else: width[i] = 0

max_width = max(width)
max_index = width.index(max_width)

print(max_index, max_width)
    

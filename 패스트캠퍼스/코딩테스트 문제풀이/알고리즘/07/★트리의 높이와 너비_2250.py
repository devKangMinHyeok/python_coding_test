import sys
input = sys.stdin.readline

class Node :
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
        self.col = -1
        self.row = -1


n = int(input())
tree = {}
table = {}
col_index = 1
height = 1

for _ in range(n):
    val, left, right = map(int, input().split())
    table[left] = True
    table[right] = True
    tree[val] = Node(val, left, right)


root = 0

for i in range(1,n+1):
    if i not in table: 
        root = i
        break
    
def inOrder (node):
    global col_index
    if node.left != -1: inOrder(tree[node.left])
    node.col = col_index
    col_index += 1
    if node.right != -1: inOrder(tree[node.right])

inOrder(tree[root])

def bfs(node, level):
    global height
    if height < level: height = level
    if node.val == -1: return
    node.row = level
    if node.left != -1: bfs(tree[node.left], level+1)
    if node.right != -1: bfs(tree[node.right], level+1)

bfs(tree[root], 1)

matrix = [[] for _ in range(height+1)] 

for key in tree:
    node = tree[key]
    matrix[node.row].append(node.col)

for i, level_arr in enumerate(matrix):
    if not level_arr: 
        matrix[i] = 0
        continue
    matrix[i] = max(level_arr) - min(level_arr) + 1

max_width = max(matrix)

for i, num in enumerate(matrix):
    if max_width == num: 
        print(i, max_width)
        break
    
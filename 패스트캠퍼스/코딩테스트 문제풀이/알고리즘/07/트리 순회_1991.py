import sys
input = sys.stdin.readline

n = int(input())
graph = {}
for _ in range(n):
    root, left, right = map(str, input().split())
    graph[root] = (left, right)

preOrders = []
inOrders = []
postOrders = []

def preOrder (left, right, val):
    if val == '.': return
    preOrders.append(val)
    if left != '.':
        preOrder(graph[left][0], graph[left][1], left)
    if right != '.':
        preOrder(graph[right][0], graph[right][1], right)

preOrder(graph['A'][0], graph['A'][1], 'A')
print("".join(preOrders))

def inOrder (left, right, val):
    if val == '.': return
    if left != '.': 
        inOrder(graph[left][0], graph[left][1], left)
    inOrders.append(val)
    if right != '.': 
        inOrder(graph[right][0], graph[right][1], right)

inOrder(graph['A'][0], graph['A'][1], 'A')
print("".join(inOrders))

def postOrder(left, right, val):
    if val == '.': return
    if left != '.': postOrder(graph[left][0], graph[left][1], left)
    if right != '.': postOrder(graph[right][0], graph[right][1], right)
    postOrders.append(val)

postOrder(graph['A'][0], graph['A'][1], 'A')
print("".join(postOrders))
       
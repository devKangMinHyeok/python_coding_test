import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    F = int(input())
    parent = {}
    number = {}
    
    def find (x) :
        if (parent[x] == x) : return x
        else :
            parent[x] = find(parent[x])
            return parent[x]
    
    def union (y,x):
        y = find(y)
        x = find(x)
        
        if y != x :
            parent[x] = y
            number[y] += number[x]    
        
    for _ in range(F):
        fr1, fr2 = map(str, input().split())
        
        if (fr1 not in parent): 
            parent[fr1] = fr1
            number[fr1] = 1
        if (fr2 not in parent): 
            parent[fr2] = fr2
            number[fr2] = 1
         
        union(fr1, fr2)
        print(number[find(fr2)])
        
        
"""
Union-Find 문제
1. find 함수
재귀적으로 그래프를 따라 흘러가서 본인을 포인팅하는 곳까지 타고 감
2. union 함수        
두 개의 노드를 받아서, 각 노드들이 최종적으로 포인팅하는 노드를 찾는다.
이 후 두 결과가 다르다면, 일정한 기준에 따라 한 노드의 포인팅을 다른 노드의 포인팅으로 바꿔주면서 같은 곳을 포인팅 하도록 한다.
+ 반면 두 결과가 같다면, 이미 같은 노드를 포인팅하고 있는 상태이다. 이 경우에는 이미 그래프로 연결되어 있다는 것이므로, union 연산이 필요없다.
"""



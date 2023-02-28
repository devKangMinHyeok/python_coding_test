import sys
input = sys.stdin.readline

N, capacity = map(int, input().split())
M = int(input())
boxes = []
table = [capacity] * (N+1)
answer = 0

for _ in range(M):
    from_id, to_id, num = map(int, input().split())
    boxes.append((from_id, to_id, num))

boxes.sort(key = lambda x : x[1])

for from_id, to_id, num in boxes:
    min_capa = float("inf")
    for i in range(from_id, to_id):
        min_capa = min(min_capa, table[i])
    if min_capa >= num :
        for i in range(from_id, to_id):
            table[i] -= num
        answer += num
    else:
        for i in range(from_id, to_id):
            table[i] -= min_capa
        answer += min_capa

print(answer)
    
    

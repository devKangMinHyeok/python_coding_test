import sys
input = sys.stdin.readline

crain = []
n = int(input())
crain = list(map(int, input().split()))
    
box = []
m = int(input())
box = list(map(int, input().split()))

crain.sort()
box.sort()

boxes = [[] for _ in range(len(crain))]
answer = 0

if max(crain) < max(box):
    print(-1)
    exit(0)

while box:
    can_use_crain = crain[:]
    while can_use_crain:
        target = can_use_crain.pop()
        for i in range(len(box)-1, -1, -1):
            if target >= box[i]:
                del box[i]
                break
    answer += 1

print(answer)
        
        
    
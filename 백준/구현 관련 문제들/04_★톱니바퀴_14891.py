from collections import deque


one = deque(list(map(int, list(input()))))
two = deque(list(map(int, list(input()))))
three = deque(list(map(int, list(input()))))
four = deque(list(map(int, list(input()))))

setter = [[], one, two, three, four]

def rotate(topni, direct):
    setter[topni].rotate(direct)
    

def is_same_right(topni):
    if topni == 4: return True
    if setter[topni][2] == setter[topni+1][6]: return True
    else: return False

def is_same_left(topni):
    if topni == 1: return True
    if setter[topni][6] == setter[topni-1][2]: return True
    else: return False

def total_rotate(topni, direct, visit):
    if visit[topni]: return
    is_right = is_same_right(topni)
    is_left = is_same_left(topni)
    rotate(topni, direct)
    visit[topni] = True
    if not is_right:
        total_rotate(topni+1, direct * -1, visit)
    if not is_left:
        total_rotate(topni-1, direct * -1, visit)
        
K = int(input())
for _ in range(K):
    visit = [False] * 5
    topni, direct = map(int, input().split())
    total_rotate(topni, direct, visit)

answer = 0
for i in range(1, 5):
    if setter[i][0] == 1: answer += 1 * pow(2, i-1)
print(answer)
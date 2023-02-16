import sys
input = sys.stdin.readline
board = []
N, M, y, x, K = map(int, input().split())
for _ in range(N):
    board.append(list(map(int, input().split())))
commands = list(map(int, input().split()))

dice = [
    0, # 윗면 (0)
    0, # 윗-동 (1)
    0, # 윗-서 (2)
    0, # 윗-남 (3)
    0, # 윗-북 (4)
    0, # 아랫면 (5)
]

def rotate(command):
    global dice
    if command == 1: # 동
        dice = [dice[2], dice[0], dice[5], dice[3], dice[4], dice[1]]
    elif command == 2: # 서
        dice = [dice[1], dice[5], dice[0], dice[3], dice[4], dice[2]]
    elif command == 3: # 북
        dice = [dice[3], dice[1], dice[2], dice[5], dice[0], dice[4]]
    else: # 남
        dice = [dice[4], dice[1], dice[2], dice[0], dice[5], dice[3]]

for command in commands:
    ny, nx = y, x
    for i, (dy, dx) in enumerate([(0,0), (0,1), (0,-1), (-1,0), (1,0)]):
        if command == i:
            ny, nx = y + dy, x + dx
    if ny < 0 or nx < 0 or ny >= N or nx >= M: continue
    rotate(command)
    if board[ny][nx] == 0:
        board[ny][nx] = dice[5]
    else:
        dice[5] = board[ny][nx]
        board[ny][nx] = 0
    y, x = ny, nx
    print(dice[0])
        
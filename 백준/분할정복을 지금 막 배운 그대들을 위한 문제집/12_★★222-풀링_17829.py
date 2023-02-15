import sys
input = sys.stdin.readline

N = int(input())
board = []

for _ in range(N):
    board.append(list(map(int, input().split())))

def solve(arr,n):
    if n == 1:
        print(arr[0][0])
    else:
        new_arr = []
        for i in range(0, n, 2):
            targets = []
            for j in range(0, n, 2):
                target = sorted([arr[i][j], arr[i][j+1], arr[i+1][j], arr[i+1][j+1]])[2]
                targets.append(target)
            new_arr.append(targets)
        solve(new_arr, n//2)

solve(board, N)
                
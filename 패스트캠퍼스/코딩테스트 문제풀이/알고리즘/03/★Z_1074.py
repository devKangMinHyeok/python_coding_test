N, Y, X = map(int, input().split())
answer = 0

def solve(size, x, y):
    global answer
    if size == 2:
        for [dy, dx] in [[0,0], [0,1], [1, 0], [1,1]]:
            ny, nx = y+dy, x+dx
            if ny == Y and nx == X:
                print(answer)
                return
            answer += 1
        return 
    next = size / 2
    for [nx, ny] in [[x,y], [x+next, y], [x, y+next], [x+next, y+next]]:
        end_ny, end_nx = ny + next - 1, nx + next - 1
        if ny > Y or nx > X or end_ny < Y or end_nx < X:
            answer += int(next ** 2)
        else: 
            solve(next, nx, ny)
    

solve(2 ** N, 0, 0)
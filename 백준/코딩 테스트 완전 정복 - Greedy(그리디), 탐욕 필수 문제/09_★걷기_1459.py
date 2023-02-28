X, Y, W, S = map(int, input().split())

x, y = 0, 0
answer = 0
if W > S:
    if abs(X-Y) % 2 == 0:
        answer = (min(X,Y) * S) + (abs(X-Y) * S)
    else:
        answer = (min(X,Y) * S) + ((abs(X-Y) -1) * S) + W
elif W * 2 <= S: # 대각선 비효율
    answer = (X+Y) * W
else: # 대각선 효율
    answer = (min(X,Y) * S) + (abs(X-Y) * W)

print(answer)
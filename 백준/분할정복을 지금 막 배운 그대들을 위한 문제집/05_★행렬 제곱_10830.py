import sys
import copy
input = sys.stdin.readline

N, B = map(int, input().split())
matrix = []
for _ in range(N):
    matrix.append(list(map(int, input().split())))

def cross(X, Y):
    new_X = copy.deepcopy(X)
    Y = copy.deepcopy(Y)
    if len(X) == 1:
        return [X[0][0] * X[0][0] % 1000]
    else:
        for i in range(len(X)):
            for j in range(len(X)):
                Sum = 0
                for k in range(len(X)):
                    Sum += (X[i][k] * Y[k][j])
                new_X[i][j] = Sum % 1000
        return new_X

def solve(X, b):
    if b == 1:
        for i in range(len(X)):
            for j in range(len(X)):
                X[i][j] = X[i][j] % 1000
        return X
    if b == 2:
        return cross(X,X)
    if b % 2:
        res = solve(X, b//2)
        return cross(cross(res, res), X)
    else:
        res = solve(X, b//2)
        return cross(res, res)

result = solve(matrix, B)

for res in result:
    print(" ".join(map(str, res)))
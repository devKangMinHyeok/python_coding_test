N = int(input())
answer = 0

def dfs(x):
    global answer
    int_x = int(x)
    if int_x > N: 
        return
    else:
        answer = max(answer, int_x)
        dfs(x + "4")
        dfs(x + "7")

dfs("0")
print(answer)
        
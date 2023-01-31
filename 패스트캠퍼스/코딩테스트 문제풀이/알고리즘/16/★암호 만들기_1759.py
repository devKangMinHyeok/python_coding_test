L, C = map(int, input().split())
chars = list(map(str, input().split()))
chars.sort()
string = []

def dfs(x):
    if len(string) == L: 
        moem = 0
        for s in string:
            if s in ['a','e','i','o','u']:
                moem += 1
        if moem >= 1 and (L - moem) >= 2: print("".join(string))
        return
    for i in range(x+1, C):
        string.append(chars[i])
        dfs(i)
        string.pop()

for i in range(C-L+1):
    string.append(chars[i])
    dfs(i)
    string = []

T = int(input())

def able(data):
    for i in range(n-1):
        if len(data[i]) >= len(data[i+1]):
            continue
        if data[i] == data[i+1][:len(data[i])]:
            return False
    return True

for _ in range(T):
    n = int(input())
    data = []
    for _ in range(n):
        data.append(input())
    data.sort()
    if able(data): print("YES")
    else: print("NO")
    
    
    
            
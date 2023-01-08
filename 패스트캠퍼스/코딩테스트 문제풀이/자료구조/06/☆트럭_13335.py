n, w, L = map(int, input().split())
trucks = list(map(int, input().split()))
line = []

weight = 0
inBridge = 0
time = 0

while (n) :
    time += 1
    if line: 
        line = [(l[0]+1, l[1]) for l in line]
        if line[0][0] > w: 
            off = line.pop(0)
            n -= 1
            weight -= off[1]
            inBridge -= 1
    if (trucks and trucks[0]+weight <= L and inBridge+1 <= w):
        on = (1, trucks.pop(0))
        line.append(on)
        weight += on[1]
        inBridge += 1

print(time)
    
        

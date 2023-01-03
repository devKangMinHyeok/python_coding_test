data = list(map(int, input().split()))

prev = data[0]
asc = True
des = True

for i in range(1,len(data)):
    num = data[i]
    if (prev < num): des = False
    elif (prev > num): asc = False
    prev = num

if (asc): print("ascending")
elif (des): print("descending")
else : print("mixed")
    
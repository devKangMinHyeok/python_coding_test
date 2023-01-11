birds = int(input())
num = 1
time = 0

while birds:
    if num > birds: num = 1
    birds -= num
    num += 1
    time += 1

print(time)
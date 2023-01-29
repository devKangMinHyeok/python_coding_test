change = 1000 - int(input())
answer = 0

for num in [500,100,50,10,5,1]:
    answer += change // num
    change = change % num

print(answer)
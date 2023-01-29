num = int(input())
remain = 1000 - num

answer = 0

def next_remain(remain, num):
    global answer
    next = remain // num
    answer += next
    remain -= num * next
    return remain

while remain:
    if remain >= 500:
        remain = next_remain(remain, 500)
    elif remain >= 100:
        remain = next_remain(remain, 100)
    elif remain >= 50:
        remain = next_remain(remain, 50)
    elif remain >= 10:
        remain = next_remain(remain, 10)
    elif remain >= 5:
        remain = next_remain(remain, 5)
    elif remain >= 1:
        remain = next_remain(remain, 1)
print(answer)
        
        
        
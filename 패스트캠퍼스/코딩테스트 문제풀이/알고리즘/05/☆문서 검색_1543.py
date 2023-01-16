total = input()
target = input()

start = 0
end = len(target) - 1
answer = 0

while end <= len(total)-1:
    sliced = total[start:end+1]
    if sliced == target:
        answer += 1
        start = end + 1
        end = start + len(target) - 1
    else:
        start += 1
        end += 1

print(answer)

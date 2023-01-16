strings = input()
target = input()
count = 0
while (target in strings):
    t_index = strings.index(target)
    strings = strings[:t_index] + " " + strings[t_index+len(target):]
    count += 1
print(count)
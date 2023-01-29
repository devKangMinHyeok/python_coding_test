tile = input()
com_tile = ""
prev = ""
for i in range(len(tile)):
    if not len(com_tile):
        prev = tile[i]
        com_tile += prev
    else:
        if prev != tile[i]:
            prev = tile[i]
            com_tile += prev

zero_num = 0
for i in range(len(com_tile)):
    if com_tile[i] == "0":
        zero_num += 1
one_num = len(com_tile) - zero_num
print(min(zero_num, one_num))
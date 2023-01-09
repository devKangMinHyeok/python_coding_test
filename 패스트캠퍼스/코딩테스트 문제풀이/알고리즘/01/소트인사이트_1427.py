inputs = input()
data = [int(i) for i in inputs]
data.sort(reverse=True)
for num in data: print(num, end="")
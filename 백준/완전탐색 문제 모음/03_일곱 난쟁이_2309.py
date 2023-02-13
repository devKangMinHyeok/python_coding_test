from itertools import combinations
data = []
for _ in range(9):
    data.append(int(input()))

data.sort()
result = combinations(data, 7)
for res in result:
    if sum(res) == 100:
        print("\n".join(map(str, res)))
        break
        
from itertools import combinations

while True:
    data = list(map(int, input().split()))
    k = data[0]
    if k == 0: break
    S = data[1:]
    result = combinations(S, 6)
    for res in result:
        for num in res:
            print(num, end=" ")
        print("")
    print("")
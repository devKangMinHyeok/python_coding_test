test_case = int(input())

for _ in range(test_case):
    F = int(input())
    table = {}
    for i in range(F):
        f1, f2 = map(str, input().split())
        if not (f1 in table) : table[f1] = set()
        if not (f2 in table) : table[f2] = set()
        table[f1].add(f2)
        table[f2].add(f1)
        network = set()
        
        
        print(len(table[f1]))
        
import sys
input = sys.stdin.readline

n = int(input())
db = {}

for _ in range(n):
    book = input()
    if book not in db: db[book] = 1
    else: db[book] += 1

db = sorted(db.items(), key = lambda item : (-item[1], item[0]))
print(db[0][0])
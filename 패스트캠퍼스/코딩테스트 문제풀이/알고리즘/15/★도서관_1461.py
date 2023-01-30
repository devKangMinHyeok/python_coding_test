import sys
input = sys.stdin.readline

n, m = map(int, input().split())
books = list(map(int, input().split()))

books.sort()

neg_books = []
pos_books = []
answer = 0

for book in books:
    if book < 0:
        neg_books.append(book)
    else:
        pos_books.append(book)

while pos_books:
    answer += pos_books.pop() * 2
    for i in range(m-1):
        if pos_books: pos_books.pop()

neg_books.reverse()

while neg_books:
    answer += -neg_books.pop() * 2
    for i in range(m-1):
        if neg_books: neg_books.pop()

max_val = max(max(books), -min(books))
print(answer - max_val)
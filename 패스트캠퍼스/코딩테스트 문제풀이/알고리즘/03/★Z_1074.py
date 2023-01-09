N, r, c = map(int, input().split())
length = 2 ** N
count = 0

def search (s1,s2,e1,e2):
    global count
    if e1-s1 == 1 and e2 - s2 == 1:
        if s1 == r and s2 == c: 
            print(count)
            exit(0)
        if s1 == r and e2 == c:
            print(count + 1)
            exit(0)
        if e1 == r and s2 == c:
            print(count + 2)
            exit(0)
        if e1 == r and e2 == c:
            print(count + 3)
            exit(0)
        count += 4
    else:
        offset = ((e1 - s1) + 1) // 2
        search(s1,        s2,        e1-offset, e2-offset)
        search(s1,        s2+offset, e1-offset, e2)
        search(s1+offset, s2,        e1,        e2-offset)
        search(s1+offset, s2+offset, e1,        e2)

search (0,0,length-1, length-1)
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
        nexts = [
            [s1,        s2,        e1-offset, e2-offset],
            [s1,        s2+offset, e1-offset, e2],
            [s1+offset, s2,        e1,        e2-offset],
            [s1+offset, s2+offset, e1,        e2]
        ]
        for target in nexts:
            next_s1, next_s2, next_e1, next_e2 = target
            if (next_s1 <= r and r <= next_e1 and next_s2 <= c and c <= next_e2):
                search(next_s1, next_s2, next_e1, next_e2)
            else:
                count += (next_e1 - next_s1 + 1) ** 2

search(0,0,length-1, length-1)
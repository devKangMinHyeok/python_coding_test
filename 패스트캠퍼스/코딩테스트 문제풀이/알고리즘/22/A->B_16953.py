from heapq import heappush, heappop

A, B = map(int, input().split())

queue = [(A,0)]
visit = set([A])

while queue:
    target, dist = heappop(queue)
    if target > B:
        print(-1)
        break
    if target == B: 
        print(dist+1)
        break
    multi = target * 2
    adder = int(str(target) + "1")
    if multi not in visit and multi >= 1 and multi <= 10e9:
        heappush(queue, (multi, dist+1))
        visit.add(multi)
    if adder not in visit and adder >= 1 and adder <= 10e9:
        heappush(queue, (adder, dist+1))
        visit.add(adder)

        
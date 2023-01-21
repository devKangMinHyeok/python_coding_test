from collections import deque

n, k = map(int, input().split())

queue = deque([(n,0)])
visit = [False] * 100001
visit[n] = True

if n == k:
    print(0)
    exit(0)

while queue:
    point, level = queue.popleft()
    for d_point in [point - 1, point + 1, point * 2]:
        if d_point >= 0 and d_point <= 100000 and not visit[d_point]:
            queue.append((d_point, level + 1))
            visit[d_point] = True
            if d_point == k:
                print(level+1)
                exit(0) 
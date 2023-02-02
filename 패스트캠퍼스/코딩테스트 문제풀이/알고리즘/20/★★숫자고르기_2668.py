N = int(input())
data = [-1] * (N+1)
visit = [False] * (N+1)
cycles = []

for i in range(1,N+1):
    data[i] = int(input())

def isCycle(x):
    global cycles
    visit[x] = True
    cycle.append(x)
    next_x = data[x]
    if visit[next_x]:
        if next_x in cycle:
            start = cycle.index(next_x)
            cycles += cycle[start:]
        return
    else:
        isCycle(next_x)
        

for i in range(1, len(data)):
    if not visit[i]:
        cycle = []
        isCycle(i)
print(len(cycles))
cycles.sort()
print("\n".join([str(i) for i in cycles]))
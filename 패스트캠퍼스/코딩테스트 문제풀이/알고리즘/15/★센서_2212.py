import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
sensors = list(map(int, input().split()))
sensors.sort()

distances = []
for i in range(len(sensors)-1):
  distances.append(abs(sensors[i] - sensors[i+1]))

distances.sort()

for i in range(k-1): 
  if distances: distances.pop()

print(sum(distances))
import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
place = list(map(int, input().split()))
place.sort()
if n == 1: 
  print(0)
  exit(0)
distance = [abs(place[i] - place[i+1]) for i in range(len(place)-1)]
distance.sort()

for _ in range(k-1):
  distance.pop()
print(sum(distance))
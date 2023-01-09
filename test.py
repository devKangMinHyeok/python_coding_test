from heapq import nsmallest, nlargest

print(nsmallest(3, [4, 1, 7, 3, 8, 5])[-1])
# 4 

print(nlargest(3, [4, 1, 7, 3, 8, 5])[-1])
# 5
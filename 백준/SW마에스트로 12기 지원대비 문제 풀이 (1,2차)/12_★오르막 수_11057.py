N = int(input())

DP = [1] * 10
print(DP)
for i in range(1,N):
    for j in range(0,10):
        sum_ = 0
        for k in range(j+1,10):
            sum_ += DP[k]
        DP[j] = DP[j] + sum_
    print(DP)

print(sum(DP) % 10007)

"""
1
0  => 1
1  => 1
2 
3 
4 
5 
6 
7 
8 
9

2
00 01 02 03 04 05 06 07 08 09 => 1 + (9-0)
11 12 13 14 15 16 17 18 19 => 1 + (9-1)
22 23 24 25 26 27 28 29 => 1 + (9-2)


3
000 001 002 ... 011 012 013 ...
111
"""
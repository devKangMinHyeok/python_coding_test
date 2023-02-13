N = int(input())
remain = 1000000000
DP = [[0] * 10 for _ in range(N+1)]
for i in range(1, 10):
    DP[1][i] = 1
if N == 1:
    print(9)
    exit(0)
for i in range(1, 10):
    DP[2][i] = 2
DP[2][9] = 1
for i in range(3,N+1):
    DP[i][1] = (DP[i-2][1] + DP[i-1][2]) % remain
    for j in range(2,9):
        DP[i][j] = (DP[i-1][j-1] + DP[i-1][j+1]) % remain
    DP[i][9] = DP[i-1][8]

print(int(sum(DP[N]) % remain))

"""
1:
1 2 3 4 5 6 7 8 9
=> 9
+8

2:
12 10
21 23
32 34
43 45
54 56
65 67
76 78
87 89 
98
=> 17
+15

3:
123 121 101
210 212 234 232
321 323 345 343
432 434 456 454
543 545 567 565
654 656 678 676
765 767 789 787
876 878 898
987 989 
=> 32

4:
1234 1232 1210 1212 1012 1010


9876 98
"""

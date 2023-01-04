max_ = -10000
winner = -1
for i in range(5):
    data = list(map(int, input().split()))
    sum_ = sum(data)
    if (sum_ > max_) :
        max_ = sum_ 
        winner = i+1

print(winner, max_)
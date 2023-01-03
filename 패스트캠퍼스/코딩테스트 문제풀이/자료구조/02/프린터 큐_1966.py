num_test = int(input())
    
def sol () :
    answer = 1
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    maxNum = max(data)
    i = 0
    while (True) :
        i %= n
        if (maxNum == data[i]) :
            if (i == m) : return answer
            else :
                data[i] = 0
                maxNum = max(data)
                answer += 1
        i += 1
            

for i in range(num_test):
    print(sol()) 
    
        
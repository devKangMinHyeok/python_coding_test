T = int(input())



def make (arr, index, last):
    if index == last:
        answers.append(arr)
    elif arr[index] == '':
        arr1 = arr[:]
        arr2 = arr[:]
        arr1[index] = '+'
        arr2[index] = '-'
        make(arr, index+1, last)
        make(arr1, index+1, last)
        make(arr2, index+1, last)
    else:
        make(arr, index+1, last)

def eval (arr):
    newArr = []
    numStr = ""
    for i in range(len(arr)):
        if i == len(arr)-1: 
            numStr += str(arr[i])
            newArr.append(int(numStr))
        elif (isinstance(arr[i], int)):
            numStr += str(arr[i])
        elif arr[i] == "+" or arr[i] == "-":
            newArr.append(int(numStr))
            newArr.append(arr[i])
            numStr = ""
    return newArr

def cal(arr_):
    arr = arr_[:]
    for i in range(len(arr)):
        if arr[i] == "+":
            arr[i] = arr[i-1] + arr[i+1]
            arr[i-1] = 0
            arr[i+1] = 0
        elif arr[i] == "-":
            arr[i] = arr[i-1] - arr[i+1]
            arr[i-1] = 0
            arr[i+1] = 0
    return sum(arr)

for _ in range(T):
    answers = []
    n = int(input())
    arr = []
    for i in range(1,n+1):
        arr.append(i)
        arr.append('')
    arr.pop()
    
    make(arr,0,len(arr)-1)
    for ans in answers:
        newAns = eval(ans)
        if not cal(newAns):
            for i,t in enumerate(newAns):
                if len(str(t)) >= 2: 
                    t = str(t)
                    for i in range(len(t)-1):
                        print(t[i], "", end="")
                    print(t[-1], end="")
                else: print(t, end="")
            print("")
    
    print("")
            
        
    
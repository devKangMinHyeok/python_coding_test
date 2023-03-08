L, K, C = map(int, input().split())
# L : 통나무 길이, K: 위치의 개수, C: 최대 통나무 자르는 횟수
locations = list(set(list(map(int, input().split()))))
locations.sort()
# 구해야 하는 것  : 가장 긴 조각을 최소로 만들고 그 길이를 구하기, 처음 자르는 위치가 가장 작은 케이스
# 전략 : 
# 1. 특정 길이를 가장 긴 조각의 길이라고 가정
# 2. 그 길이로 잘랐을 때, 통나무를 자른 횟수 구하기
# 3. 만약 그 횟수가 최대 횟수보다 작다면, 더 자를 수 있기 때문에 더 짧은 길이로 다시 탐색
# 4. 만약 그 횟수가 최대 횟수보다 크다면, 존재할 수 없는 케이스이기 때문에 더 큰 길이로 다시 탐색
# 5. 최소가 되는 가장 긴 길이를 구했을 때, 그 길이를 기반으로 뒤에서 부터 자르기
# 6. 뒤에서부터 자르는 이유는 가장 처음 자르는 것은 길이가 넉넉해서 길게 자르지만, 마지막에는 짧게 자르게 때문

def check(length):
    acc = 0
    prev = 0
    slice_location = [0]
    
    for loc in locations:
        acc += loc - prev
        if acc > length:
            slice_location.append(prev)
            acc = loc - prev
        elif acc == length:
            slice_location.append(loc)
            acc = 0    
        prev = loc
    slice_location.append(L)
    table = []
    for i in range(len(slice_location)-1):
        table.append(slice_location[i+1]-slice_location[i])

    if max(table) > length: return False
    if len(slice_location)-2 <= C: return True
    else: return False

def binary_search():
    low = 1
    high = L
    ans = -1 # 최소가 되는 가장 긴 길이
    while low <= high:
        mid = (low + high) // 2
        if check(mid): # 가능 + 더 자를 수 있는 경우
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans
    
def slice(length):
    acc = 0
    prev = L
    slice_location = []
    locations.insert(0, 0)
    for loc in reversed(locations):
        acc += abs(prev - loc)
        if acc > length:
            slice_location.append(prev)
            acc = abs(loc - prev)
        elif acc == length:
            slice_location.append(loc)
            acc = 0
        prev = loc
    
    slice_location.sort()
    print(slice_location)
    if slice_location[0] == 0: return slice_location[1]
    else: return slice_location[0]
        
            
min_long_length = binary_search()
print(min_long_length, slice(min_long_length))
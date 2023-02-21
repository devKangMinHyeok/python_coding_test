# python_coding_test

## Skills

### 접근

> 데이터의 개수가 많지 않은 경우
>
> -> 문제에서 요구하는 대로 단순하게 구현한다

> Stack
>
> Stack을 사용하는 경우 두가지 로직을 핵심으로 사용한다.
>
> 어떠한 조건에 의해 pop을 반복적으로 수행하는 것
>
> Stack의 top과 비교하여 이 반복작업을 멈출지 판단하는 것
>
> 즉, Stack의 상단의 원소와의 비교가 핵심이다.

---

### input

아래 코드를 사용하면, input 명령을 빠르게 실행할 수 있다.
특히 여러줄을 반복적으로 input을 받을 때, 더 빠르게 받을 수 있다.

(백준에서는 이 명령어를 안써서 맞는 코드도 시간초과가 발생하는 경우가 있다.)

```python
import sys
input = sys.stdin.readline
```

---

### print

리스트 한번에 print할때

```python
result = ['1','2','3']
print('\n'.join(result))

# ----print----
# 1
# 2
# 3
```

---

### List

서로 다른 list를 합칠때

```python
list1 = [1,2]
list2 = [3,4]
result = list1 + list2
# [1,2,3,4]
```

```python
list1 = [1,2]
list2 = [3,4]
list1.extend(list2)
print(list1)
# [1,2,3,4]
```

리스트를 뒤집을 때

```python
prime_numbers = [2, 3, 5, 7]
print(prime_numbers.reverse()) # reverse는 pop처럼 return 값이 있지 않다.
# None
print(prime_numbers)
# [7, 5, 3, 2]
```

```python
numbers = [1,2,3,4,5]
print(list(reversed(numbers)))
# [5, 4, 3, 2, 1]

strings = "string"
print(list(reversed(strings)))
# ['g', 'n', 'i', 'r', 't', 's']
```

주어진 리스트를 튜플 형태의 리스트로 변환할 때

```python
queue = [1,3,6,2,4]
queue = [(i, num) for i, num in enumerate(queue)]
# [(0, 1), (1, 3), (2, 6), (3, 2), (4, 4)]
```

---

### 얕은 복사 vs 깊은 복사

** 얕은 복사: ** '참조'만 복사 (주소 값 복사)
** 깊은 복사: ** '실제 값'을 '새로운' 메모리에 복사

**Point**

- immutable 객체 (int, float 등)

  값이 변경되면 주소가 바뀌기 때문에, 고려 X

- mutable 객체(list, set, dictionary 등)

  mutable 객체는 얕은 복사, 깊은 복사 주의 필요!

**Usage**

`=` : 얕은 복사

`[:]`, `copy()`, `copy.copy()` : 반만 깊은 복사, 다중 리스트의 경우는 내부 리스트가 얕은 복사로 가져와짐

`copy.deepcopy` : 깊은 복사 (내부 요소까지 완벽히 새로운 메모리에 할당)

---

### string

**String to List**

```python
a= "I love python"
print(a.split()) #공백을 기준으로 나눈다.

>>['I','love','python']
```

```python
a='I/love/python'
print(a.split('/'))

>>['I', 'love', 'python']
```

```python
a="I love python"
print(list(a))

>>['I', ' ', 'l', 'o', 'v', 'e', ' ', 'p', 'y', 't', 'h', 'o', 'n']
```

```python
a=['I','love','python']
print("".join(a)) # 각 요소를 공백없이 붙인다.
print(" ".join(a)) # 요소사이에 공백을 추가.
print("\n".join(a)) # 한줄에 하나씩.

>>Ilovepython
>>I love python
>>I
>>love
>>python
```

### upper, lower, title, capitalize, swapcase

- upper은 모든 문자를 대문자로
- lower은 모든 문자를 소문자로
- title은 각 단어의 첫 글자를 대문자로, 나머지는 소문자로
- capitalize는 첫 글자만 대문자로, 나머지는 소문자로
- swapcase는 대문자는 소문자로, 소문자는 대문자로

```python
a = 'a,b,c,D,E'

print(a.upper())
# A,B,C,D,E

print(a.lower())
# a,b,c,d,e

inputStr = "ByungJun And Jiwon"

swapcaseStr = inputStr.swapcase()
print(swapcaseStr)
#bYUNGjUN aND jIWON
```

### count, find, index, startwith, endswith

**count**

- 먼저, count 함수는 특정 문자의 개수를 반환
- count내에 두 번째 인자로 숫자를 지정해준다면, 해당 위치 인덱스를 시작점으로 탐색

**find**

- find 함수는 해당 문자가 처음으로 등장하는 인덱스를 반환
- 해당 문자를 찾지 못하면 -1을 반환
- 두 번째 인자에 숫자를 넣어주면, 해당 위치부터 탐색을 시작하여 가장 처음 해당 문자가 등장하는 인덱스를 반환

**index**

- index 함수는 find 함수와는 사용법이 거의 동일
- 해당 문자를 찾지 못하면 -1을 반환하는 것이 아니라, 에러를 발생

```python
inputStr = "아기 판다와 어른 판다는 둘 다 판다입니다"

print(inputStr.count("판다"))
#3

print(inputStr.find("판다"), inputStr.rfind("판다"), inputStr.find("판다", 6), inputStr.find("불곰"))
#3 18 10 -1

print(inputStr.index("판다"), inputStr.rindex("판다"), inputStr.index("판다", 6))
#3 18 10

print(inputStr.startswith("아기"), inputStr.startswith("사자"), inputStr.startswith("판다", 3), inputStr.endswith("판다입니다"))
#True False True True
```

### isdigit, isalpha, isupper, islower

- isdigit은 모든 문자열이 숫자이면 True
- isalpha는 모두 알파벳이거나 한글이면 True
- isupper, islower은 각각 모두 대문자, 소문자로 구성인지 여부로 True를 반환 (단, isupper, islower에서는 각각 소문자, 대문자만 안섞여있다면 이와 상관없는 숫자, 공백 등의 문자는 결과에 상관이 없습니다.)

### strip, rstrip, lstrip, replace

문자열에서 공백을 제거할 수 있는 함수들은 strip, rstrip, lstrip이 있으며,

줄바꿈 문자(\n)이나 tab문자(\t) 등도 포함하여 제거가 가능합니다.

- rstrip은 오른쪽 끝, lstrip은 왼쪽 끝의 공백을 제거
- strip 함수는 양쪽 끝의 공백을 모두 제거

```python
a = '   abc   '
print(a.strip()) # 'abc'
print(a.lstrip()) # 'abc   '
print(a.rstrip()) # '   abc'

a = '*****abc***'
print(a.strip('*')) # abc
print(a.lstrip('*')) # abc***
print(a.rstrip('*')) # *****abc

a = '12321abc111'
print(a.strip('123')) # abc
print(a.lstrip('123')) # abc111
print(a.rstrip('123')) # 12321abc
```

- replace 함수는 특정 문자를 다른 문자로 대체

```python
a = 'a,b,c,d,e'
print(a.replace(',', '/')) # a/b/c/d/e
print(a.replace(',', '/', 1)) # a/b,c,d,e
print(a.replace(',', '/', 2)) # a/b/c,d,e
```

---

# Data Structure

### deque

```python
from collections import deque

deq = deque()

# Add element to the start
deq.appendleft(10)

# Add element to the end
deq.append(0)

# Pop element from the start
deq.popleft()

# Pop element from the end
deq.pop()
```

```python
# Contain 1, 2, 3, 4, 5 in deq
deq = deque([1, 2, 3, 4, 5])

deq.rotate(1)
print(deq)
# deque([5, 1, 2, 3, 4])

deq.rotate(-1)
print(deq)
# deque([1, 2, 3, 4, 5])
```

---

### heapq

```python
from heapq import heappush, heappop

heap = []

heappush(heap, 4)
heappush(heap, 1)
heappush(heap, 7)
heappush(heap, 3)

print(heap)
# [1,3,7,4]

print(heappop(heap))
# 1

print(heap)
# [3,7,4]
```

```python
from heapq import heapify

heap = [4, 1, 7, 3, 8, 5]
heapify(heap)
print(heap)
# [1, 3, 5, 4, 8, 7]
```

```python
from heapq import nsmallest, nlargest

print(nsmallest(3, [4, 1, 7, 3, 8, 5])[-1])
# 4

print(nlargest(3, [4, 1, 7, 3, 8, 5])[-1])
# 5
```

---

# Functions

### max, min 함수

```python
max(x)
min(x)
```

x 는 반복이 가능한 데이터 타입 (문자열, 리스트, 튜플)

```python
# min(iterable) 함수 예제1 : 리스트 이용
a = [1, 2, 3]
print(min(a))  # 반환 : 1

# min(iterable) 함수 예제2 : 문자열 이용
b = 'BlockDMask'
print(min(b))  # 반환 : 'B'

# min(iterable) 함수 예제3 : non iterable 인 경우
c = 1
# print(min(c))  # error : 'int' object is not iterable

# min(iterable) 함수 예제4 : 튜플 이용
d = (6, 5, 4, 2)
print(min(d))  # 반환 : 2

# min(iterable) 함수 예제5 : 리스트 이용2
e = [3, 4, 5, 'a', 'b', 'c']
# print(min(e))  # error : str 타입과 int 타입은 비교할 수 없기 때문
```

여러개의 iterable 객체를 넣을 수도 있음

```python
# min(arg1, arg2) 함수 예제1 : 리스트
a = [1, 2, 3]
b = [4, 5, 6]
print(min(a, b))   # 반환 : [1,2,3]

# min(arg1, arg2) 함수 예제2 : 문자열
c = 'BlockDMask'
d = 'BAAAlockDMask'
print(min(c, d))   # 반환 : 'B'

# min(arg1, arg2) 함수 예제3 : 타입이 다른 경우
e = [3, 2, 1]
f = ['a', 3, 2, 1]
# print(min(e, f)) # error
# TypeError: '<' not supported between instances of 'str' and 'int'

# min(arg1, arg2, ...) 함수 예제4 : 인자가 N 개
g = [2, 3, 4]
h = [2, 2, 2, 2, 2]
i = [9, 8, 7, 6, 5]
j = [1]
k = [0]
print(min(g, h, i, j, k))   # 반환 : [0]
```

---

### sort, sorted

sorted는 기존의 리스트를 변경하는 것이 아니라 정렬된 새로운 리스트를 반환한다.

```python
list1 = [4, 2, 3, 5, 1]

print(sorted(list1))
# [1, 2, 3, 4, 5]

print(list1)
# [4, 2, 3, 5, 1]

```

리스트의 메소드인 sort()를 사용하여도 정렬이 된다. 이 경우에는 리스트 자체를 변경해 버린다.

```python
list1 = [4, 2, 3, 5, 1]
list1.sort()

print(list1)
# [1, 2, 3, 4, 5]
```

sort()는 리스트만을 위한 메소드이지만 sorted() 함수는 어떤 이터러블 객체도 받을 수 있다.

```python
students = [
        ('홍길동', 3.9, 2016303),
        ('김철수', 3.0, 2016302),
        ('최자영', 4.3, 2016301),
]

print(sorted(students, key=lambda student: student[2]))
# [('최자영', 4.3, 2016301), ('김철수', 3.0, 2016302), ('홍길동', 3.9, 2016303)]
```

list.sort()와 내장함수 sorted()는 모두 reverse 매개변수를 받는다. reverse 변수는 부울형으로 True 이면 내림차순이 된다.

```python
students = [
        ('홍길동', 3.9, 2016303),
        ('김철수', 3.0, 2016302),
        ('최자영', 4.3, 2016301),
]

print(sorted(students, key=lambda student: student[2], reverse=True))
# [('홍길동', 3.9, 2016303), ('김철수', 3.0, 2016302), ('최자영', 4.3, 2016301)]
```

my_dict.items()를 출력해보면 다음과 같이 Tuple pair로 이루어진 List가 리턴된다.

```python
my_dict = {'c': 3, 'a': 1, 'b': 2, 'e': 1, 'd': 2}
print(my_dict.items())
# dict_items([('c', 3), ('a', 1), ('b', 2), ('e', 1), ('d', 2)])
```

Dictionary sort는 다음과 같이 수행된다.

key를 기준으로 정렬

```python
my_dict = {'c': 3, 'a': 1, 'b': 2, 'e': 1, 'd': 2}

sorted_dict = sorted(my_dict.items(), key = lambda item: item[0])
print(sorted_dict)
# [('a', 1), ('b', 2), ('c', 3), ('d', 2), ('e', 1)]
```

item을 기준으로 정렬

```python
sorted_dict = sorted(my_dict.items(), key = lambda item: item[1])
print(sorted_dict)
# [('a', 1), ('e', 1), ('b', 2), ('d', 2), ('c', 3)]
```

다중 정렬

```python
a = [(1, 2), (0, 1), (5, 1), (5, 2), (3, 0)]

# key 인자에 함수를 넘겨주면 해당 함수의 반환값을 비교하여 순서대로 정렬한다.
c = sorted(a, key = lambda x : x[0])
# c = [(0, 1), (1, 2), (3, 0), (5, 1), (5, 2)]
d = sorted(a, key = lambda x : x[1])
# d = [(3, 0), (0, 1), (5, 1), (1, 2), (5, 2)]

# 아이템 첫 번째 인자를 기준으로 오름차순으로 먼저 정렬하고,
# 그리고 그 안에서 다음 두 번째 인자를 기준으로 내림차순으로 정렬하게 하려면, 다음과 같이 할 수 있다.
e = [(1, 3), (0, 3), (1, 4), (1, 5), (0, 1), (2, 4)]
f = sorted(e, key = lambda x : (x[0], -x[1]))
# f = [(0, 3), (0, 1), (1, 5), (1, 4), (1, 3), (2, 4)]
```

---

### lambda

```python
keys = [{'key': 8}, {'key': 5}, {'key': 9}, {'key': 3}]

# sort 함수
keys.sort(key = lambda x: x['key'])
# [{'key': 3}, {'key': 5}, {'key': 8}, {'key': 9}]

# max 함수
arr = [(0,10),(1,14),(2,2),(3,24)]
str = max(arr, key = lambda x: x[1])
# (3,24)

# filter 함수
my_list = [12, 65, 54, 39, 102, 339, 221, 50, 70, ]
result = list(filter(lambda x: (x % 13 == 0), my_list))
# [65, 39, 221]

```

---

### combination

```python
import itertools

arr = ['A', 'B', 'C']
nCr = itertools.combinations(arr, 2)
print(list(nCr))

# 결과 : [('A', 'B'), ('A', 'C'), ('B', 'C')]
```

### permutation

```python
import itertools

arr = ['A', 'B', 'C']
nPr = itertools.permutations(arr, 2)
print(list(nPr))

# 결과 : [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]
```

---

### bisect

```python
from bisect import bisect_left, bisect_right

nums = [0,1,2,3,4,5,6,7,8,9]
n = 5

print(bisect_left(nums, n))
print(bisect_right(nums, n))

'''
결과값
5
6
'''
```

```python
from bisect import bisect_left, bisect_right

nums = [4, 5, 5, 5, 5, 5, 5, 5, 5, 6]
n = 5

print(bisect_left(nums, n))
print(bisect_right(nums, n))


'''
결과값
1
9
'''
```

---

### exit

exit을 사용하면, 어디에서나 프로그램을 종료할 수 있다.

함수가 아닌 경우, return으로 종료할 수 없으므로, 이럴 때 사용할 수 있다.

```python
exit(0)
```

---

### eval

문자열로 표현되어 있는 표현식의 값을 평가해서 리턴하는 함수

```python
exp = "1 + 2"
result = eval(exp)

print(result)
# 3
```

---

### ord

하나의 '문자'를 인자로 받아서 해당하는 유니코드 '정수'를 반환한다.

```
ord('a')
# 97
```

### chr

하나의 '정수'를 인자로 받아서 해당하는 유니코드 '문자'를 반환한다.

```
char(97)
# 'a'
```

---

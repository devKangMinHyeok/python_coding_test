# python_coding_test

## Skills

### 접근

> 데이터의 개수가 많지 않은 경우
>
> -> 문제에서 요구하는 대로 단순하게 구현한다

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

### exit

exit을 사용하면, 어디에서나 프로그램을 종료할 수 있다.

함수가 아닌 경우, return으로 종료할 수 없으므로, 이럴 때 사용할 수 있다.

```python
exit(0)
```

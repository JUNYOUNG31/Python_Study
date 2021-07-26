# day6_1

## 데이터 구조

### 데이터 구조

순서가 있는 데이터 구조(시퀀스)

문자열

리스트



순서가 없는 데이터 구조(비시퀀스)

세트

딕셔너리

---

### 문자열

(immutable)변경불가능

(ordered)순서있음

(iterable)순회가능

인덱스(index)

자르기 ( Slicing )

a   b   c

0   1   2

-3 -2  -1

s[start:stop:step]



문자열 조회/탐색

```python
문자열.find(x)
# x의 첫번째 위치를 반환. 없으면 -1 반환
'apple'.find('p')
=>1
'apple'.find('k')
=>-1
```

```python
문자열.index(x)
# x의 첫번째 위치를 반환. 없으면 오류발생
'apple'.index('p')
=>1
'apple'.index('k')
=>ValueError
```

문자열 변경

```python
문자열.replace(old,new[,count])#대괄화부분을 배우진 않았다(선택적 인자)
							  #배커스-나우르 표기법(참고용)
#바꿀 대상 글자를 새로운 글자로 바꿔서 변환(복사본 반환)
'coone'.replace('o','a')
=>'caane'
'wooooowoo'.replace('o','!',2)
=>'w!!ooowoo'
```

```python
문자열.strip([chars])
#특정한 문자들을 지정하면, 양쪽을 제거하거나(strip),
#왼쪽을 제거하거나(lstrip),오른쪽을제거(rstrip)
#문자열을 지정하지 않으면 공백을 제거

```

```python
문자열.split(sep=none)
#문자열을 특정한 단위로 나눠 리스트로 반환
'a,b,c'.sprit('_')
=>['a,b,c']
'a b c'.split()
=>['a','b','c']
```

```python
'separator'.join(iterable)
#반복가능한 컨테이너 요소들을 separator(구분자)로 합쳐 문자열 반환
'!'.join('ssafy')
=>'s!s!a!f!y'
' '.join(['3','5'])
=>'3 5'
```

```python
.capitalize() : 앞글자를 대문자로
.title() : '나 공백 이후를 대문자로
.upper() : 모두 대문자로
.lower() : 모두 소문자로
.swapcase() : 대<->소문자로 변경하여
```

문자열 관련 검증 메소드

```python
.isalpha() : 알파벳 문자 여부
.isupper() : 대문자 여부
.islower() : 소문자 여부
.istitle() : 타이틀 형식 여부
```

```python
.isdecimal() < .indigit() < .isnumeric()
```

---

### 리스트

순서가 있는 시퀀스, 인덱스로 접근

문자열의 특징

(mutable)변경가능

(ordered)순서있음

(iterable)순회가능



값 추가 및 삭제

추가

```python
.append(x)
#리스트에 값을 추가
```

```python
.extend(iterable)
#리스트에 iterable의 항목을 추가
```

```python
.insert(i,x)
#정해진 위치 i 에 값을 추가
```

삭제

```python
.remove(x)
#리스트에서 값이 x인 것 삭제
```

```python
.pop(i)
#정해진 위치 i에 있는 값을 삭제하고, 그항목을 반환함
#i가 지정되지 않으면, 마지막 항목을 삭제하고 반환
```

```python
.clear()
#모든 항목을 삭제
```

탐색 및 정렬

```python
.index(x)
#값을 찾아 해당 index 값을 반환. 없을경우 ValueError
```

```python
.count(x)
#원하는 값 x의 개수를 반환
```

```python
.sort()
#원본 리스트를 정렬함. None 반환
#내장함수 sorted 함수와 비교하면 sort는 원본을 놔두고 정렬된 리스트를 반환
```

```python
.reverse()
#원본의 순서를 반대로 뒤집음
```

리스트 복사

( 주의 )리스트의 복사는 같은 리스트의 주소를 참조한다.

해당 주소의 일부 값을 변경하는 경우 이를 참조하는 모든 변수에 영향



리스트 복사 - 얕은 복사(shallow copy)

1. slice 연산자 활용하여 같은 원소를 가진 리스트지만 연산된 결과를 복사(다른 주소)

```python
a = [1,2,3]
b= a[:]
print(a,b)
b[0] = 5
print(a,b)
```

2. list() 활용하여 같은 원소를 가진 리스트지만 연산된 결과를 복사(다른 주소)

```python
a = [1,2,3]
b = list(a)
print(a,b)
b[0] = 5
print(a,b)
```

주의 사항

복사하는 리스트의 원소가 주소를 참조하는 경우



리스트 복사 - 깊은 복사(deep copy)





list comprehension

표현식과 제어문을 통해 특정한 값을 가진 리스트를 생성하느 법

```python
[<expression> for <변수> in <iterable>]
[<expression> for <변수> in <iterable> if <조건식>]
```

자주 사용하진 않지만

바꾸는 법을 알아두는 것이 좋다



built-in Function -map

```python
map(function, iterable)
#순회 가능한 데이터 구조의 모든 요소에 함수적용.그결과를 map object로 반환
#리스트 형변환을 통해 결과 직접 확인
```



```python
filter(function, iterable)
#순회 가능한 데이터 구조의 모든 요소에 함수적용.그결과를 True인 것들을 filter object로 반환
#리스트 형변환을 통해 결과 직접 확인
```



```python
zip(*iterables)
#복수의 iterable을 모아 튜플을 원소로 하는 zip object를 반환
#리스트 형변환을 통해 결과 직접 확인
```



---

### 세트

중복 없이 순서가 없는 데이터 구조

(mutable)변경가능

(unordered)순서없음

(iterable)순회가능

```python
.add(elem)
# 세트에 값을 추가
```

```python
.update(*others)
# 여러 값을 추가
```

```python
.remove(elem)
#세트에서 삭제하고 없으면 keyError
```

```python
.discard(elem)
#세트에서 삭제하고 없어도 에러가 발생하지 않음
```

```python
.pop()
#임의의 원소를 제거해 반환
```

---

### 딕셔너리

key 와 value로 구성된 데이터 구조

(mutable)변경가능

(unordered)순서없음

(iterable)순회가능



조회

```python
.get(key[,default])
#key를 통해 value를 가져옴
#keyError가 발생하지 않음. default 값을 설정할 수 있음 (기본:None)
```

추가 및 삭제

```python
.pop(key[,default])
#key가 딕셔너리에 있으면 제거하고 해당 값을 반환. 아니면 default 반환
#default 값이 없으면 KeyError
```

```python
.update()
#값을 제공하는 key, value로 덮어쓴다
```



딕셔너리 순회

딕셔너리는 기본적으로 key를 순회하며,  key 를 통해 값을 활용



보통 추가 매서드를 활용하여 순회한다

```python
key() : key로 구성된 결과
values() : value로 구성된 결과
items() : (key,value)의 튜플로 구성된 결과
    
grades = {'john': 80, 'eric':90}
for name, score in grades.items():
    print(name,score)
=> john 80
=> eric 90
```



Dictionary Comprehension

```python
{key : value for <변수> in <iterable>}

{key : value for <변수> in <iterable> if <조건식>}
```

---

simple is better than complex 

코트의 가독성은 코드의 간결함보다 훨씬 더 중요한 목표

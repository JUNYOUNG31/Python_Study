# day3_1

## 함수

### 함수 기초

내장함수 활용

pstdev 함수 ( 파이썬표준 라이브러리 - statistics)



함수 기본 구조

이름

매개변수

함수 바디

반환값  return



Docstring(Document String)

함수나 클래스의 설명



함수의 선언

def 키워드를 사용

```python
def foo():
    return True
def add(x, y):
    return x + y
```

---

### 함수 output

함수의 리턴(return)

함수는 항상 반환되는 값이 있으며, 어떠한 객체라도 상관없음

오직 한 개의 객체만 return 됨

​	복수의 객체를 return 하는 경우 => 복수의 객체를 하나의 tuple로 변환

​	명시적인 return 값이 없는 경우 => None 타입을 반환



주의

return은 함수 안에서만 사용되는 키워드

print는 출력을 위해 사용되는 함수



---

### 함수 input (  중요 )

위치 인자

기본적으로 함수 호출 시 인자는 위치에 따라 함수 내에 전달된다

매개변수와 인자의 차이?

```python
#parameter(매개변수)

#함수에 입력으로 전달된 값을 받는 변수

def my_func(a,b):

pass

#argument(위치 인자)

#함수를 호출할 떄 함수에 전달하는 입력 값

my_func(1,2)


```



기본 인자 값

기본값을 지정하여 인자 값을 설정하지 않도록 함

```python
def add(x, y=0):
    return x + y

add(2)

def add(x, y=0):
    x=2
    return x + y
```



키워드 인자



```python
def add(x, y):
    return x + y 

add(x=2, y=5)
add(y=5, x=2)
```



정해지지 않은 여러개의 인자 처리

가변 인자 리스트

'*' packing

*kargs

가변 키워드 인자

인자들은 딕셔너리로 묶여 처리된다. '**' packing

**kwargs



---

### 함수 Scope



LEGB



global





기본적으로 함수에서 선언된 변수는 Local scope 에 생성되며 함수 종료 시 사라짐



해당 스코프에 변수가 없는 경우 LEGB rule 에 의해 이름을 검색함

​	변수에 접근은 가능하지만, 해당 변수를 수정할 수는 없음

​	값을 할당하는 경우 해당 스코프의 이름공간에 새롭게 생성되기 때문



상위 스코프에 있는 변수를 수정하고 싶다면 global, nonlocal 키워드를 활용 가능

​	코드가 복잡해지면서 변수의 변경을 추적하기 어렵고,얘기치 못한 오류가 발생	

​	가급적 사용하지 않는 것을 권장,함수로 값을 바꾸고자 한다면 항상 인자로 넘기고 리턴 값을 사용하	는 것을 추천




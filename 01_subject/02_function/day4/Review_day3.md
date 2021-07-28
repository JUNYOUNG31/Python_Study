# Review_day3

## workshop

### 1. list 합 구하기

```python
num =[1,2,3,4,5]
#파라미터로는 숫자리스트
#반환으로는 정수형을 반환
                 #type 힌트 설명일뿐 함수에 영향을 주진않는다.
def list_sum(arr:list)->int:  # _  스네이크 형식
    ans = 0
    for i in arr:
        ans+=i
    return ans

print(list_sum(num))
    
```



### 2. dictionary 로 이루어진 list 합구하기

```python
def dict_list_sum(i): #i =>리스트
    total = 0
    for a in i:  # a=> 딕셔너리
        total += a['age']
    return total

print(dict_list_sum([{'name': 'kim', 'age': 18},
                     {'name': 'park', 'age': 6}])) 
```



### 3. 2차원 list의 합 구하기

```py
def all_list_sum(i):
	total = 0
	#2차원 리스트에서 1차원씩 넣기
	for a in i:
		for num in a:
			total += num
	return total

print(all_list_sum([[1],[2,3],[4,5,6],[7,8,9,10],[11,12,13,14,15]]))
```



## homework

### 2. 정중앙 문자

```python
def get_middle_char(word):
    mid = len(word) // 2 # int 안쓰고 몫을 바로 반환하면됨
    #홀
    if len(word) % 2:
        return word[mid]
    else:
        return word[mid-1:mid+1] #슬라이싱
```



### 4.나의 반환값은

```python
def my_func(a,b):
    c = a + b
    print(c)

result = my_func(5,6)

# return 값이 없기때문에 result에는 none 이 반환된다.
```



### 5. 가변인자를 이용한 평균

```python
def my_avg(*args):
    return sum(args) /len(args)

print(my_avg(77, 85, 95, 92, 71, 90))
```


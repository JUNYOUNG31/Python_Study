# day18

## 알고리즘

### 2차원 배열

```python
N, M =map(int, input().split())
arr =[list(map(int, input().split())) for _ in range(N)]

arr2 = [[0]*M for _ in range(N)]
arr2 = [[0]*M]*N => 사용불가 다른의미의 이차원 배열
```



---

### 배열 순회

1. 행 우선 순회

   ```python
   # i  행의 좌표
   # j  열의 좌표
   for i in range(len(array)):
   	for j in range(len(array[i])):
   		array[i][j] # 필요한 연산 수행
   ```

2. 열 우선 순회

   ```python
   # i  행의 좌표
   # j  열의 좌표
   for j in range(len(array[0])):
   	for i in range(len(array)):
   		array[i][j] # 필요한 연산 수행
   ```

3. 지그재그 순회

   ```python
   # i  행의 좌표
   # j  열의 좌표
   for i in range(len(array)):
   	for j in range(len(array[0):
   		array[i][j+(m-1-2*j)*(i%2)]
           # 필요한 연산 수행
   ```



---

### 델타를 이용한 2차 배열 탐색

4방향의 인접 배열 요소를 탐색

```python
arr[0...n-1][0..n-1]
dx = [-1, 1, 0 ,0]  # 상하좌우
dy = [0, 0, -1, 1]

for i in range(len(arr)):
    for j in range(len(arr[i])):
        for k in range(4): # 4방향
            testX = x+dx[k]
            testY = x+dy[k]
            test(arr[testX][testY])
```



---

전치 행렬

```python
# i : 행의 좌표, len(arr)
# j : 열의 좌표, len(arr[0])
arr = [[1,2,3],[4,5,6],[7,8,9]]  # 3*3 행렬

for i in range(3):
    for j in range(3):
        if i<j:
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
```



### 부분집합

loop를 이용하여 생성

```python
bit=[0,0,0,0]
for i in range(2):
    bit[0] = i					# 0번째 원소
    for j in range(2):
        bit[1] = j				# 1번째 원소
        for k in range(2):
            bit[2] = k			# 2번째 원소
            for l in range(2):
                bit[3] = l		# 3번째 원소
                print(bit)		# 생성된 부분집합 출력       
```



비트 연산자

``` python
&   비트 단위로 and 연산
|	비트 단위로 or  연산
<<  피연산자의 비트 열을 왼쪽으로 이동
>>	피연산자의 비트 열을 오른쪽으로 이동

1<<n  2n 즉 원소가 n개일 경우의 모든 부분집합의 수를 의미

i &(i<<j)  i의 j 번째 비트가 1인지 아닌지를 리턴
```



간결하게 부분집합 생성

```python
arr = [ 3, 6, 7, 1, 5, 4]	
n = len(arr)				# n : 원소의 개수
for i in range(1<<n):		# 1<<n : 부분 집합의 개수
    for j in range(n):      # 원소의 수만큼 비트를 비교함
        if i & (i<<j): 		# i 의 j 번째 비트가 1이면 j번째 원소 출력
            print(arr[j], end=", ")
    print()
print()
```



### 검색

검색의 종류

* 순차 검색
  * 정렬되어 있지 않는 경우
  * 정렬 되어 있는 경우
* 이진 검색
* 해쉬

---

### 순차 검색

일렬로 되어 있는 자료를 순서대로 검색하는 방법



정렬되어 있지 않은 경우

* 검색 과정

  * 첫번째 원소부터 순서대로 검색 대상과 키 값이 같은 원소가 있는지 비교
  * 키 값이 동일한 원소를 찾으면 그 원소의 인덱스를 반환
  * 자료구조의 마지막에 이를 때까지 찾지못하면 검색 실패

* 찾고자 하는 원소의 순서에 따라 비교회수가 결정됨

* ```python
  def sequentialSearch( a, n, key):
      i = 0
      while i< n and a[i] != key:
          i = i+1
      if i < n : return i
      else : return -1     
  ```



정렬되어 있는 경우

* 검색과정

  * 자료가 오름차순으로 정렬된 상태에서 검색을 실시한다고 가정
  * 자료를 순차적으로 검색하면서 키 값을 비교하여 원소의 키 값이 검색대상의 키 값보다 크면 찾는 원소가  업다는 것이므로 더이상 검색하지 않고 검색 종료

* 찾고자 하는 원소의 순서에 따라 비교회수가 결정됨

  * 정렬되어있어서 정렬되지않은것보다 검색실패를 반환하는 회수가 줄어듬

* ```python
  def sequentialSearch2( a, n, key):
      i = 0
      i = i+1
      while i<n and i[i]<key:
          i = i+1
      if i<n and a[i] = key: return i
      else: return -1
  ```



---

### 이진 검색

* 자료의 가운데에 있는 항목의 키 값과 비교하여 다음 검색의 위치를 결정하고 검색을 진행
  * 목적 키를 찾을 때까지 이진 검색을 순환적으로 반복 수행함으로써 검색 범위의 반으로 줄여가면서 빠르게 검색
* 이진 검색을 하기 위해서는 자료가 정렬된 상태여야 한다.



* 검색 과정

  * 자료의 중앙에 있는 원소를 선택

  * 중앙 원소의 값과 찾고자 하는 목표 값을 비교

  * 목표 값이 중앙 원소의 값보다 작으면 자료의 왼쪽 반에 대해서 새로 검색 수행

    크다면 자료의 오른쪽 반에 대해서 검색 수행

  * 찾고자 하는 값을 찾을때 까지 반복

* ```python
  def binarySearch(a, key):
      start = 0 
      end = len(a)-1
      while start<=end:
          middle =(start + end)//2
          if a[middle] == key:
              return midlle
          elif a[middle] > key:
              end = middle -1
          else:
              start = middle +1
      return -1
  arr= [2,4,7,9,11,19,23]
  print(binarySearch(arr,11))
  ```



* 재귀 함수 이용

* ```python
  def binarySearch2(a, low, high, key):
      if low > high :
          return False
      else:
          middle = (low + high)//2
          if key == a[middle]:
              return True
          elif key < a[middle]:
              return binarySearch2(a, low, middle-1, key)
          elif key > a[middle]:
              return binarySearch2(a, middle+1, high, key)
  ```



---

### 인덱스

* 배열을 사용한 인덱스
  * 대량의 데이터를 매번 정렬하면, 프로그램의 반응이 느려지기때문에 배열 인덱스를 사용



### 선택 정렬

* 주어진 자료들 중 가장 작은 값의 원소부터 차례대로 선택하여 위치를 교환하는 방식

* 정렬 과정

  * 주어진 리스트중에 최소값을 찾는다
  * 그 값을 리스트 맨 앞에 위치한 값과 교환한다
  * 맨 처음 위치를 제외한 나머지 리스트를 대상으로 반복

* 알고리즘

* ```python
  def SelectionSort(a[], n)
  	for i from 0 to n-1
      	a[i],...,a[n-1] 원소 중 최소값 a[k] 찾음
          a[i]와 a[k] 교환 
  ```

* ```python
  #구현
  def SelectionSort(a):
      for i in range(0, len(a)-1):
          min = i
          for j in range(i+1, len(a)):
              if a[min]>a[j]:
                  min = j
          a[i], a[min] = a[min],a[i]



---

### 셀렉션 알고리즘

* 저장되어 있는 자료로부터 k번째로 큰 또는 작은 원소를 찾는 방법
  * 최소값, 최대값, 중간값을  찾는 알고리즘
* 선택 과정
  * 자료 정렬
  * 원하는 순서에 있는 원소 가져오기
  * 

```python
# 연습문제 3번 알고리즘
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

N= 5
cnt = 1
i, j = 0, -1
k = 0
while cnt <= N*N:
    ni, nj = i+di[k], j+dj[k]
    if ni, nj가 유효하고 and a[ni][nj] == 0
        a[ni][nj] = cnt
        cnt += 1
    i , j = ni, nj
    else
        k = (k+1)% 4
```






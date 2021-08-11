# day17

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
    for j in range(n+1):    # 원소의 수만큼 비트를 비교함
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
* 이전 검색
* 해쉬

---

순차 검색

일렬로 되어 있는 자료를 순서대로 검색하는 방법


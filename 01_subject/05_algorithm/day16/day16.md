# day15

## 알고리즘

표현방식 =>> 슈더 코드 , 순서도



### 알고리즘의 이해

* 정확성 : 얼마나 정확하게 동작하는가

* 작업량 : 얼마나 적은 연산으로 원하는 결과를 얻어내는가

* 메모리 사용량 : 얼마나 적은 메모리를 사용하는가

* 단순성 : 얼마나 단순한가

* 최적성 : 더 이상  개선할 여지없이 최적화되었는가

  

### 성능 측정

* 시간복잡도 => 빅-오 표기법

  O(n!) >> O(2^n) >> O(n^2) >> O(nlogn) >> O(n) >> O(logn) >> O(1)



## 배열

1차원 배열 

Arr = list()      or     Arr = []



### 버블 정렬

인접한 두개의 원소를 비교하며 자리를 계속 교환하는 방식

```python
def Bubblesort(a):                               # 숫자 정렬 함수 설정
    for i in range(len(a) - 1, 0, -1):
        for j in range(0, i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a
```





### 카운팅 정렬

항목들의 순서를 결정하기 위해 집합에 각 항목이 몇 개씩 있는지 세는 방식

```python
nums = list(map(int, input().split()))        
counts = [0] * (K + 1)
# 카운팅 하기
for i in range(len(nums)):
	counts[nums[i]] += 1
# 누적합 counts 리스트
for i in range(1, len(counts)):
	counts[i] += counts[i - 1]
```



### 완전 탐색

모든 경우의 수를 나열해보고 확인하는 기법

brute-force 브루트포스라고도 불림



### 순열 ( P )

서로 다른 것들 중 몇개를 뽑아서 한 줄로 나열

nPr 

```python
for i1 in range(1,4):
    for i2 in range(1,4):
        if i2 != i1 :
            for i3 in range(1,4):
                if i3 != i1 and i3 != i2:
                    print(i1, i2, i3)
```


# Review_day2

## sort() 와 sorted()  차이

```python
arr=[5,2,1,6,7,8]
#sort() 원본을 바꾼다. 반환값은 없음
#arr.sort()

#sorted() 원본을 바꾸지 않고, 정렬된 리스트를 반환해준다.
#sort_arr = sorted(arr)
```



## 평균 구하기

```python
cnt = 0
total = 0
for score in scores:
    total + = score
    cnt += 1
print(total/cnt)
```


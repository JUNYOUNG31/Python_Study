# 1. Built-in 함수와 메서드
new_sort = [1,5,6,2,3,4]
result1 =new_sort.sort()  # 원본 변경
print(new_sort.sort()) 
print(new_sort,result1) # 원본을 변경했기때문에 none 값 반환


new_sorted = [1,4,6,5,2,3]
result2 = sorted(new_sorted)  # 원본이 아닌 새로값을 반환
print(new_sorted,result2)     # 원본은 변경이 없다

# 2. .extend()와 .append()
fruit = ['사과','바나나','수박','딸기']
fruit.append('오렌지') # append 는 항목을 값을 추가하고
fruit.extend('포도')   # 항목에 문자열 각각의 항목이 추가된다.

print(fruit)

# 3. 복사가 잘 된 건가?

a = [1,2,3,4,5]
b =a 

a[2] = 5

print(a)
print(b)

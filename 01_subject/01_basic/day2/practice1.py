#갯수 구하기
students = ['철수', '영희', '민지','순재','문희']

len(students)

# cnt 변수를 하나 두어서 직접 체크
cnt = 0
for i in students:
    print(i)
    cnt += 1

print(cnt)
###############################################################################

#순재의 갯수 구하기
students = ['영희', '순재', '순재', '민지', '철수', '순재', '영희', '문희']

students.count('순재')

#반복문 + 조건문을 이용해서 카운트 해보자. 
cnt = 0 # 초기화
#반복문 수행
for st in students:   
    if st == '순재':
        cnt += 1
print(cnt)

#인덱스 접근
cnt = 0
for idx in range(len(students)):
    if students[idx] == '순재':
        cnt += 1
        
print(cnt)
###############################################################################

#최댓값 구하기
numbers = [5, 11, 23, 4, 1, 16, 32, 19, 21]
max(numbers)

#문제를 꼼꼼하게 읽어보고 해야할것 ... 
#만약 문제에서 -100 ~ 100까지 라고 했을 때 음수로만 구성된 리스트가 존재하면 0으로 초기화 할시 틀리게 된다. 
max_value = 0 # 최댓값을 구할땐 0으로 설정

for i in numbers:
    if i > max_value:
        max_value = i
    
print(max_value)
###############################################################################


#최솟값 구하기
numbers = [5, 11, 23, 4, 1, 16, 32, 19, 21]
min(numbers)

min_value = 987654321 # 최솟값을 구할땐 큰 수로 임의 설정
for i in range(len(numbers)):
    if min_value > numbers[i]:
        min_value = numbers[i]

print(min_value)
###############################################################################

#최댓값 등장횟수
numbers = [5, 11, 23, 32, 11, 16, 32, 19, 21]
print(max(numbers), numbers.count(32))


#초기화 굉장히 중요
max_value = numbers[0]
count = 1
#리스트 순회
for i in range(1, len(numbers)):
    if numbers[i] > max_value:
        max_value = numbers[i]
        count = 1
    elif numbers[i] == max_value:
        count += 1

print(max_value, count)
###############################################################################

#임의의 수 갯수 구하기
numbers = [7, 12, 16, 22, 18, 9, 5, 9, 15]

# 아래에 코드를 작성하시오.
print(numbers.count(9))

cnt = 0 # 초기화
#반복문 수행
for num in numbers:    
    if num == 9:
        cnt += 1
print(cnt)
###############################################################################

#해당 문자 삭제하고 표현 'a'
word = input()
for char in word:
    if char == 'a':
        continue
    print(char,end='')
print()

result = ''
for char in word:
    if char != 'a':
        result += char

print(result)
###############################################################################

#단어 뒤집기
word = input()
i = len(word)
while i > 0:
    print(word[i-1], end = '')
    i -= 1
print()

for i in range(len(word)-1,-1,-1):
    print(word[i], end='')

#swap
#reverse
#join 등 많이 있음
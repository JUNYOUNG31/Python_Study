#입력한 값의 약수 구하기
N = int(input())
if 1<=N and N <= 1000:
    for i in range(1, N + 1):
        if  N % i == 0: 
            print(i , end=' ')
else:
    print('숫자를 잘못 입력하였습니다.')


#중간값 찾기
numbers = [
    85, 72, 38, 80, 69, 65, 68, 96, 22, 49, 67,
    51, 61, 63, 87, 66, 24, 80, 83, 71, 60, 64,
    52, 90, 60, 49, 31, 23, 99, 94, 11, 25, 24
]
numbers.sort()
print((numbers[int(len(numbers)/2)]))

#계단 만들기
number = int(input())
for i in range(1,number+1):
    for i in range (1,i+1):
        print(i, end=' ')
        i+=1
    print()
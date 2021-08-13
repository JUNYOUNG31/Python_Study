# Flatten
def Bubblesort(a):                               # 숫자 정렬 함수 설정
    for i in range(len(a) - 1, 0, -1):
        for j in range(0, i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a


for case in range(10):                          # 케이스 반복
    dump = int(input())                         # dump 수입력
    data = list(map(int, input().split()))      # data 입력
    for d in range(dump):                       # 덤프 만큼 반복
        Bubblesort(data)                        # 숫자를 정렬하고
        data[0] += 1                            # 제일작은수 +1
        data[-1] -= 1                           # 제일큰수 -1

    Bubblesort(data)                            # 최종 정렬
                                                # 마지막수 - 처음수
    print("#{} {}".format(case+1, data[-1]-data[0]))
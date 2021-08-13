# hamberger = ['패티', '양상추', '치즈', '피클', '양파']
hamberger = ['패티', '양상추', '치즈', '피클']

N = len(hamberger)
for i in range(1 << N):
    # i 는 부분집합의 경우의수 이진수로 생각....
    for j in range(N):
        if i & (1 << j):
        #여기에 걸렸다는 해당 j번째 비트가 1이라는 뜻이고
        # 값이 존재한다는 듰이다.
            print(hamberger[j], end=" ")
    print()
    # print(" 를 가진 햄벜 냠냠")


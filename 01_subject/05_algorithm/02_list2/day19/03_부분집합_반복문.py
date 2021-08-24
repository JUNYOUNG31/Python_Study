bit = [0, 0, 0, 0]
for i in range(2) :
    bit[0] = i                  # 0번째 원소
    for j in range(2) :
        bit[1] = j              # 1번째 원소
        for k in range(2) :
            bit[2] = k          # 2번째 원소
            for l in range(2) :
                bit[3] = l      # 3번째 원소
                print(bit)      # 생성된 부분집합 출력

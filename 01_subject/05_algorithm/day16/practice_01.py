T = int(input())                    # 테스트 개수
for case in range(T):               # case 반복
    num = int(input())              # 숫자 입력
    counts = [0]*12                 # 숫자를 저장할 counts 리스트를 0부터 12까지 저장
                                    # 3개를 탐색하기 때문에 9에서 인덱스에러발생 방지를 위해 12까지 늘림
    for i in range(6):              # 6자리 숫자를 counts 에 저장
        counts[num % 10] += 1       # 10으로 나눈 나머지를 추가
        num = num // 10             # 몫을 저장

    triplet = 0                     # 트리플 수  같은 숫자가 3개일 때
    run = 0                         # 런 수      연속된 숫자가 3개일 때
    i = 0
    while i < 10:                   # 0에서 9까지 반복
        if counts[i] >= 3:          # 같은수가 3개일 경우
            triplet += 1            # triplet + 1
            counts[i] -= 3          # 숫자 3개삭제
            continue                # 그다음 진행
        if counts[i] >= 1 and counts[i+1] >= 1 and counts[i+2] >= 1:    # 연속된 3개의 숫자가 1개씩 있을때
            run += 1                # run + 1
            counts[i] -= 1          # 각 숫자 1개삭제
            counts[i+1] -= 1        # 각 숫자 1개삭제
            counts[i+2] -= 1        # 각 숫자 1개삭제
            continue
        i += 1                      # 1증가

    if run + triplet == 2:          # 두합이 2이면 baby gin = 1 반환
        print("#{} {}".format(case+1, 1))
    else:                            # 두합이 2가아니면 0 반환
        print("#{} {}".format(case+1, 0))


# 완전  탐색
nums =[1, 2, 3, 5, 5, 5]
is_ok = False
for i in range(6):
    for j in range(6):
        if j != i:
            for k in range(6):
                if k != j and k != i:
                    for l in range(6):
                        if l != k and l != j and l != i:
                            for m in range(6):
                                if m != l and m != k and m != j and m != i:
                                    for n in range(6):
                                        if n != m and n != l and n != k and n != j and n != i:
                                            print(nums[i], nums[j], nums[k], nums[l], nums[m], nums[n])
                                            left = False
                                            right = False

                                            # 왼쪽을 tri , run 검사
                                            if nums[i] == nums[j] == nums[k]:
                                                left = True
                                            elif nums[i] == nums[j]-1 == nums[k]-2:
                                                left = True

                                            # 오른쪽도 작성
                                            if nums[l] == nums[m] == nums[n]:
                                                right = True
                                            elif nums[l] == nums[m]-1 == nums[n]-2:
                                                right = True

                                            if left and right:
                                                is_ok = True


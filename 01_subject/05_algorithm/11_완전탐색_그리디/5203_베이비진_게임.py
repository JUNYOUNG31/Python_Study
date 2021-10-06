# 베이비진 게임

# 1부터 9까지인 숫자 카드 4세트를 섞은 후 6개의 카드를 골랐을 때, 연속인 숫자가 3개 이상이면
# run, 같은 숫자가 3개 이상이면 triplet이라고 한다. 게임을 시작하면 플레이어1과 플레이어 2가 교대로 한 장
# 씩 카드를 가져가며, 6장을 채우기 전이라도 먼저 run이나 triplet이 되는 사람이 승자가 된다. 두 사람이 가져가게
# 되는 순서대로 12장의 카드에 대한 정보가 주어졌을 때 승자를 알아내는 프로그램을 작성하시오.
# 만약 무승부인 경우 0을 출력한다. 예를 들어 9 9 5 6 5 6 1 1 4 2 2 1인 경우, 플레이어 1은 9, 5, 5, 1, 4, 2카드를,
# 플레이어2는 9, 6, 6, 1, 2, 1을 가져가게 된다.이때는 카드를 모두 가져갈 때 까지 run이나 triplet이
# 없으므로 무승부가 된다.

# 첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50
# 다음 줄부터 테스트 케이스의 별로 각 줄에 0에서 9사이인 12개의 숫자가 주어진다.


def baby_jin(person):                   # baby jin 확인
    i = 0                               # 카드
    while i < 10:                       # 반복
        if person[i] >= 3:              # 같은게 3장이면
            return 1                    # 1 리턴
        elif i >= 2 and person[i-2] and person[i-1] and person[i]:  # 연속한 3개가 있다면
            return 1                    # 1 리턴
        i += 1                          # i 증가
    return 0                            # 다돌아도 결과가 안나면


T = int(input())                             # case 입력
for tc in range(1, T+1):                     # case 반복
    card = list(map(int, input().split()))   # 카드 입력
    person1 = [0] * 10                       # 카드의 개수를 담을 인덱스 사람1
    person2 = [0] * 10                       # 카드의 개수를 담을 인덱스 사람2
    ans = 0                                  # 정답
    for i in range(12):                      # 12장 반복
        if i % 2 == 0:                       # 짝수면
            person1[card[i]] += 1            # 1번 플레이어 카드 수 입력
            if baby_jin(person1) == 1:       # babyjin 확인
                ans = 1                      # 1이 나오면 ans = 1승리
                break                        # 멈춰
        else:                                # 홀수면
            person2[card[i]] += 1            # 2번 플레이어 카드 수 입력
            if baby_jin(person2) == 1:       # 확인
                ans = 2                      # 1 나오면 ans = 2 승리
                break                        # 멈춰
    else:                                    # 0이 리턴되면 무승부
        ans = 0
    print("#{} {}".format(tc, ans))

# 최대 상금

def money(idx, x):                                  # 재귀함수
    global ans                                      # 정답
    if x == change:                                 # 다 바꾸면
        ans = max(int(''.join(nums)), ans)          # 정답에 붙여서 추가한다
        return
    for i in range(idx, len(nums)):                 # 완전탐색해서
        for j in range(i+1, len(nums)):
            if nums[i] <= nums[j]:                  # 앞자리가 더작으면
                nums[i], nums[j] = nums[j], nums[i] # 뒷자리랑 바꾼다
                money(i, x+1)                       # 재귀로 계속해서 깊이 들어간다.
                nums[i], nums[j] = nums[j], nums[i] # 다돌고나서 다시 돌려놓기
    if ans == 0:                                    # 답에 아직 값이 없으면
        nums[-1], nums[-2] = nums[-2], nums[-1]     # max 값이긴하니깐 맨뒤에 2개를 자리 바꾼다.
        x += 1                                      # 카운트 1 증가하고
        money(idx, x)                               # 다시 돌리기


T = int(input())                                    # case 개수
for tc in range(1, T+1):                            # case 반복
    num, change = map(int, input().split())         # 숫자랑 바꿀 횟수 입력
    nums = list(str(num))                           # 숫자를 리스트화
    ans = 0                                         # 정답
    money(0, 0)                                     # 완전 탐색 시작
    print("#{} {}".format(tc, ans))                 # 정답 출력
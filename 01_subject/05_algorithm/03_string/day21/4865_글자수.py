# 글자수
T = int(input())                        # case 수
for tc in range(1, T+1):                # case 반복
    N = list(map(str, input()))         # N 을 입력
    M = list(map(str, input()))         # M 을 입력
    cnt = [0]*len(N)                    # N의 길이 만큼 카운트할 리스트
    max_cnt = 0                         # cnt의 최대값
    for i in range(len(N)):             # N의 값들을 반복하고
        for j in range(len(M)):         # M의 값들을 반복해서
            if N[i] == M[j]:            # 두값이 같다면
                cnt[i] += 1             # cnt 리스트의 i 에 1씩 추가한다
    for k in range(len(N)):             # cnt 리스트를 반복해서
        if cnt[k] > max_cnt:            # 최대값을 뽑고
            max_cnt = cnt[k]
    print("#{} {}".format(tc, max_cnt)) # 출력한다
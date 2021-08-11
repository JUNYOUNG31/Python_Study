T = int(input())
for case in range(T):
    B = int(input())
    box = list(map(int, input().split()))
    area = []
    for i in box:
        if i != 0:
            area.append('1'*i + '0'*(B-i+1))
        if i == 0:
            area.append('0'*B)
    print(area)

    print(area[0][(box[0])-1])   # 첫번째 box의 제일 높은 층의 box 값


####
T = int(input())
for case in range(T):
    N = int(input())
    box = list(map(int, input().split()))
    ans = 0

    for i in range(N):
        cnt = 0

        for j in range(i+1, N):
            if box[i] > box[j]:
                cnt += 1

        if ans < cnt:
            ans = cnt
    print("#{} {}".format(case+1, ans))
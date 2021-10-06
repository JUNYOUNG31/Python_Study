# 수영장
def price(cost, m):                     # 가격
    global min_cost                     # 최소가격
    if m > 12:
        if min_cost > cost:
            min_cost = cost
        return
    price(cost + day*month[m], m+1)     # 1일 이용권으로 가격
    price(cost + month1, m+1)           # 1달 이용권으로 가격
    price(cost + month3, m+3)           # 3달 이용권으로 가격


T = int(input())                        # case 입력
for tc in range(1, T+1):                # case 반복
    day, month1, month3, year = map(int, input().split())  # 가격 입력
    month = [0] + list(map(int, input().split()))          # 월 이용 계획
    min_cost = year
    price(0, 1)
    print("#{} {}".format(tc, min_cost))
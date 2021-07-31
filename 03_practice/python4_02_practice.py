#2.1 종합소득세 계산하기
# A라는 나라에서는 종합소득세는 과세표준 금액 구간에 따라 다른 세율이 적용된다.
# 즉, 1,300만원을 벌었을 경우 1,200*0.06 + 100*0.15를 계산한 결과가 납부해야 하는 세액이다.
# 납부해야하는 세금의 결과를 반환하는 함수 tax()를 작성하시오.
def tax(won):
    money = 0
    if won > 4600 :
        money =  582 + (won-4600)*0.35
    elif won > 1200 :
        money = 72 + (won-1200)*0.15
    else:
        money = won*0.06
    return money

print(tax(1200))
print(tax(4600))
print(tax(5000))


# 2.2 카쉐어링 요금 계산하기
# 카쉐어링 서비스는 요금을 다음과 같이 계산한다.
# 대여는 10분 단위로 가능하다.
# 대여 요금 : 10분당 1,200원
# 보험료 : 30분당 525원 (50분을 빌리면, 1시간으로 계산)
# 주행 요금 : km당 170원 (주행 요금은 100km가 넘어가면, 넘어간 부분에 대하여 할인이 50% 적용)
# 예) 160km를 달렸으면, 170*100 + 85 *60
# 양의 정수인 대여시간(분)과 주행거리를 받아 계산 결과를 반환하는 함수 fee()를 작성하시오.
def fee(minute, distance):
    don_min = (1200*(minute//10)) + (525*round(minute/30))
    don_dis = 0
    if distance > 100 :
        don_dis = 170*100 + 85*(distance-100)
    else:
         don_dis = 170*distance
    
    return don_min + don_dis
   
print(fee(600, 50))
print(fee(600, 110))

# 2.3문자열 탐색
def start_end(words):
    count =0
    for word in words:
        if len(word)>=2:
            if word[0] == word[-1]:
                count +=1
    return count

print(start_end(['level', 'asdwe', 's', 'abceda', 'gsdwrtfg']))

# 2.4 Collatz 추측 
# 1937년 Collatz란 사람에 의해 제기된 이 추측은, 주어진 수가 1이 될때까지 다음 작업을 반복하면, 모든 수를 1로 만들 수 있다는 추측이다. 그 원리는 아래와 같다.
# 입력된 수가 짝수라면 2로 나눈다.
# 입력된 수가 홀수라면 3을 곱하고 1을 더한다.
# 결과로 나온 수에 같은 작업을 1이 될 때까지 반복한다.
# 예를 들어, 입력된 수가 6이라면 6 → 3 → 10 → 5 → 16 → 8 → 4 → 2 → 1 이 되어 총 8번 만에 1이 된다.
# 위 작업을 몇 번이나 반복해야하는지 반환하는 함수 collatz()를 작성하시오 (단, 작업을 500번을 반복해도 1이 되지 않는다면 –1을 반환하시오.)

def collatz(num):
    count = 0    
    while num != 1:        
        if num % 2 == 0:
            num = num // 2
        elif num % 2 ==1:
            num = num * 3 + 1
        count += 1            
    if count < 501:
         return count
    else:
        return -1

print(collatz(6))
print(collatz(16))
print(collatz(27))
# print(collatz(626331))

# 2.5 딕셔너리 뒤집기

def dict_invert(my_dict):
    result={}
    for key in my_dict.keys():
        try:
            result[my_dict[key]].append(key)
        except:
            result[my_dict[key]] = [key]
     
    
    return result



print(dict_invert({1: 10, 2: 20, 3: 30}))
print(dict_invert({1: 10, 2: 20, 3: 30, 4: 30}))
print(dict_invert({1: True, 2: True, 3: True}))
# 1. 무엇이 중복일까
def duplicated_letters(fruit):       
    what = []  # 리스트를 이용한 방법
    for i in fruit: 
        count = fruit.count(i)    
        if count > 1 and not( i in what): # 중복값을 제거 한다.
            what += [i]
                     
    return what

print(duplicated_letters('apple'))
print(duplicated_letters('banana'))


def duplicated_letters(fruit):
    obj = {}    # 딕셔너리를 이용한 방법
    for char in fruit:
        try:
            obj[char] = obj[char] + 1
        except:
            obj[char] = 1

    return [key for key in obj.keys() if obj[key] >= 2]


# 2.소대소대
def low_and_up(fruit):
    new = ''
    for i in range(len(fruit)):
        if i % 2 : #인덱스가 홀수인 부분은 대문자로
            new += fruit[i].upper() 
        else:      #인덱스가 짝수인 부분은 그대로
            new += fruit[i]
    return new
    
print(low_and_up('apple'))
print(low_and_up('banana'))

# 3. 숫자의 의미
def lonely(list_num):
    for i in range(len(list_num)-1,0,-1):  # 뒤에서부터 없애기위해 
        if list_num[i] == list_num[i-1]:   # 값이 같을때
            list_num.pop(i)                # 하나를 없앤다.
                    #remove 를 적용하니 처음부터 삭제되서 값이 다르게 반환됨
    
    return list_num

print(lonely([1,1,3,3,0,1,1]))
print(lonely([4,4,4,3,3]))
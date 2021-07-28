# 1. 숫자의 의미
def get_secret_word(num):
    name = ''
    for i in num:
        name += chr(i)
    return name
    
print(get_secret_word([83,115,65,102,89])) # =>'SsAfY'

# 2. 이름을 숫자로 변환
def get_secret_number(Name):
    Number = 0
    for i in Name:
        Number += ord(i)
    return Number

print(get_secret_number('tom'))

#3. 강한 이름

def get_strong_word( x , y):   
    num1 = 0     
    for x1 in x:
        num1 += ord(x1)
    num2 = 0
    for y1 in y:
        num2 += ord(y1)        
    if num1 < num2:
        return y
    elif num1 > num2:
        return x
    else:
        return x

print(get_strong_word('z','a'))
print(get_strong_word('tom','john'))
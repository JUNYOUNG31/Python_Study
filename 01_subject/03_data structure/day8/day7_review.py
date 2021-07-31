#2. 대소문자 변환
##########################################
def my_lower(word):
    #word 대문자라면 수정
    # if 65 <= ord(word) <= 90:
    if 'A' <= word <= 'Z':
        return chr(ord(word)+32)
    #word 소문자면 그냥 리턴
    return word

def my_upper(word):
    if 'a' <= word <='z':
        return chr(ord(word)-32)
    return word
########################################
def my_lower(word):
    Lalpha = 'abcdefghijklmnopqrstuvwxyz'
    Ualpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in range(26):
        if Ualpha[i] == word:
            ans = Lalpha[i]
            return ans
            
    return word 


# 3. 숫자의 의미
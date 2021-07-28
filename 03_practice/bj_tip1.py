# 15552번 문제 # 빠른 A + B 

# sys.stdin.readline()은 우리의 입력과 함께  \n까지 받아들입니다.
# ( 뉴라인,엔터 ), 그렇기 때문에 숫자는 괜찮습니다. (ex) int()를 통해 온전한 숫자만 얻을 수 있음 )
# 하지만 문자열의 경우엔 포함되어버리므로 문제가 된다.
# apple이라는 입력을 받고 변수 str에 넣는다
# str = input() 
# str = sys.stdin.readline()
# 1) input의 경우
# => str = apple
# 2) sys.stdin.readline의 경우
# => str = apple\n 이 된다.
# 자 이것을, 아래와 같이 다뤄본다
import sys
str = sys.stdin.readline()        # apple을 입력함

if str  == "apple":                    # str은 apple이 아니라 apple\n이므로, if문을 통과하지 못합니다.
    print("apple is right")    
    
str = input()

if str  == "apple":                    # str은 apple이므로, if문을 통과합니다.
    print("apple is right")   
        
import sys
str = sys.stdin.readline().rstrip()    

if str  == "apple":                    # str은 apple이므로, if문을 통과합니다
    print("apple is right")    

# 따라서, 오른쪽의 \n을 없애주는 rstrip() 메소드가 필요한 것! (양쪽은 strip()) 그리고 import sys도!
# 모든 경우에 사용할 수 있다. 다만, 위와 같이 문자열을 다루게 되는 순간은 조심!
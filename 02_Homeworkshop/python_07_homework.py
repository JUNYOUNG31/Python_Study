# 1. type Class
dict() str() map() int() float()

# 2. Magic Method

__init__    # 생성자를 생성하고
__del__     # 생성자를 삭제하고
__str__     # 문자열을 출력하고
__repr__    # 


# Instance Method



# Module Import

# fibo.py
def fibo_recursion(n):
    if n < 2:
        return n
    else:
        return fibo_recursion(n-1) + fibo_recursion(n-2)


from fibo import fibo_recursion as recursion

recursion(4)
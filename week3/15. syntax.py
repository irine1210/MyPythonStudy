'''
@Author  : heyheyheyJoy
@Time    : 2022/1/24 6:09 下午
@File    : 15. syntax.py
'''

def fun(a,b=10):
    print('a=',a)
    print('b=',b)

def fun1(*args):  # 个数可变的位置形参
   print(args)

def fun2(**args2):  # 个数可变的关键字形参
    print(args2)

fun(10,20)  # 位置实参传递
fun(a=10,b=20)  # 关键字实参传递

fun1(10,20,30)  # 元组 (10, 20, 30)
fun2(a=100,b=222,c=333,d=666) # 字典 {'a': 100, 'b': 222, 'c': 333}


# 函数定义时的形参顺序问题
def fun3(a,b,*,c,d,**args):  # 表示 c,d 只能按照关键字传递(**args)
    pass

def fun4(*args,**args2):  # *args ： 个数可变的位置参数； **args： 个数可变的关键字参数
    pass


def prpr(a,b):
    c=a+b   #  c 为局部变量，因为c是在函数体内进行定义的变量。a，b为函数的形参，作用范围也是函数内部，相当于局部变量
    prpr(c)

# print(c)   无法执行，因为c是局部变量，不能在函数体外使用。这句代码超出了作用域

def fun5():
    global age  # 函数内部定义的变量本应该是局部变量。但如果加上global声明，则变为了全局变量
    age=20
    print(age)

fun5()  # 20
print(age)  # 20
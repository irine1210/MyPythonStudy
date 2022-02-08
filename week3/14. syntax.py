'''
@Author  : heyheyheyJoy
@Time    : 2022/1/24 2:10 下午
@File    : 14. syntax.py
'''

'''
def cal(a,b): # a,b 是形参
    c = a+b
    return c

result = cal(10,20) # 10，20 是实参
print(result)

res = cal(b=10,a=20)


# 如果是不可变对象，在函数题内部修改不会影响实参的值  arg1=100但是n1=11仍然没变
# 如果是可变对象，在函数题内部修改会影响实参的值 arg2调用.append()，arg2=[22, 33, 44, 10],n2= [22, 33, 44, 10], n2也跟着改变了
def fun(arg1,arg2):
    print('\n原本的arg1=',arg1)
    print('原本的arg2=',arg2)
    arg1=100
    arg2.append(10)
    print('\nfun内部新的的arg1=',arg1)
    print('fun内部新的的arg2=',arg2)

n1=11
n2=[22,33,44]
fun(n1,n2)

print('\nfun外部n1=',n1)
print('fun外部n2=',n2)


# ---------------函数返回值有多个时，结果为元组
def fun(num):
    odd = []  # 存放奇数
    even = []  # 存放偶数
    for i in num:
        if i%2!=0:
            odd.append(i)
        else:
            even.append(i)
    return odd,even

print(fun([10,20,32,45,55,63,70])) # ([45, 55, 63], [10, 20, 32, 70])

def fun2():
    return 'hi','world'

res=fun2()
print(res)  # ('hi', 'world')  两个返回值，得到的就是元组
# 要不要写return视情况而定

def fun3(a,b=30):
    print(a,b)

res=fun3(10)  # 默认值不给，那就按照a=10，b=30
res2=fun3(10,20) # 如果重新给了b的值，则将b=20做计算

def fun4(*args):  # 不确定要传入几个参数，则用*来表示,只能定义一个
    print(args)

res3=fun4(20,99,00)  # (20, 99, 0)  可变的位置参数
# 一个*的结果是元组

def fun5(**args):   # 只能有一个关键字参数
    print(args)
fun5(a=10)  # {'a': 10}
fun5(a=10,b=30,c=30)   # {'a': 10, 'b': 30, 'c': 30}
# 两个*的结束是键值对

def fun6(*args1,**args):
    pass
'''


def fun(a,b,c):
    print('a=',a)
    print('b=',b)
    print('c=',c)
fun(10,20,30)
print('---------------')

lst = [10,20,30]
fun(*lst)  # 在函数调用时，将【列表中的每个元素】都转换成【位置实参】传入
print('---------------')

dic={'a':100,'b':222,'c':555}
fun(**dic)    #在调用时，将【字典中的键值】对都转换成【关键字实参】传入
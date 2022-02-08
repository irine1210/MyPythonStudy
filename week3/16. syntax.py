'''
@Author  : heyheyheyJoy
@Time    : 2022/1/25 3:16 下午
@File    : 16. syntax.py
'''

'''
def fac(n):
    if n==1:
        return 1
    else:
        return n*fac(n-1)

print(fac(6))

print('------------------')
try:
    def fib(n):  # 1,1,2,3,5,8
        if n == 1:
            return 0
        elif n == 2:
            return 1
        else:
            return fib(n - 1) + fib(n - 2)

except ValueError:
    print('搞错啦')


for i in range(1,7):
    print(fib(i))

lst = []
lst.append(11)
print(lst)

print('------------------')

try:
    a=int(input('请输入第一个数：'))
    b=int(input('请输入第二个数：'))
    res=a/b
except ZeroDivisionError:
    print('被除数不能为0')
except ValueError:
    print('只能输入数字')
else:
    print('result = ',res)
    
try:
    a=int(input('请输入第一个数：'))
    b=int(input('请输入第二个数：'))
    res=a/b
except BaseException as szy:  # 不知道可能会出现什么错，就写BaseException
    print('出错了',szy)
else:
    print(res)
finally:
    print('hi,不管是否出错都要执行这一句～')
    
'''

import traceback
try:
    print('-----------')
    print(1/0)
except:
    traceback.print_exc()  # ZeroDivisionError: division by zero
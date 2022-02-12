'''
@Author  : heyheyheyJoy
@Time    : 2022/2/8 9:29 下午
@File    : calc2.py
'''

def add(a,b):
    return a+b


# =============以主程序运行===================

if __name__  == '__main__':
    print(add(10,20))  # 只有运行calc2模块时，才会执行10+20的运算；如果你运行的是demo6模块，就不会执行add(10,20)，只会执行a+b
                       # 换言之：只有在calc2是主程序的时候才会执行这一句代码
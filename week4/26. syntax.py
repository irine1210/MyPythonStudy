'''
@Author  : heyheyheyJoy
@Time    : 2022/2/8 7:26 下午
@File    : 26. syntax.py
'''

# 模块化编程的好处：把一个任务分成n多个模块，每一个模块由不同的人员开发，有利于团队协作开发；可以实现代码复用

import math # 数学运算模块
print(type(math))
print(math.pi)
print('---------------')
print(dir(math))
print(math.pow(2,3))   # 2的3次方

print(math.ceil(9.001))    # ceil的意思是天花板，所以.ceil()方法表示向上取整
print(math.floor(9.0001))  #  floor 是地板，所以.floor()表示向下取整


print('---------------')

from math import pi
print(pi)

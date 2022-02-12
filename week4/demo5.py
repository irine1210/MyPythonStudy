'''
@Author  : heyheyheyJoy
@Time    : 2022/2/8 9:19 下午
@File    : demo5.py
'''

# 在demo中导入calc自定义模块的使用

''''
import calc
print(calc.add(1,2))   # 3
print(calc.div(2,1))   #2.0
'''

from calc import add
print(add(1,2)) # 2  注意，这里不用写成calc.add(),直接使用add()方法就行


'''
@Author  : heyheyheyJoy
@Time    : 2022/2/8 9:56 下午
@File    : demo8.py
'''

# 在demo8的模块中导入package包
import package.module1 as A  # package.module1 起一个别名，这里叫做A
                            # 导入的时候就是   包名.模块名
sum = A.calc(10,20)
print(sum)  # 130

# 方法二： from 包名 import 模块名
import sys
print(sys.getsizeof(24)) # 28个字节
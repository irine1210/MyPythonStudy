'''
@Author  : heyheyheyJoy
@Time    : 2022/1/30 4:34 下午
@File    : 25. syntax.py
'''

# 变量三要素：id、type、value

class CPU:
    pass

class Disk:
    pass

class Computer:
    def __init__(self,cpu,disk):
        self.cpu = cpu
        self.disk = disk

# (1) 变量的赋值
cpu1 = CPU()
cpu2 = cpu1
print(cpu1)
print(cpu2)


'''
@Author  : heyheyheyJoy
@Time    : 2022/1/30 2:37 下午
@File    : 23. syntax.py
'''


class Animal(object):
    def eat(self):
        print('动物会吃肉')

class Dog(Animal):
    def eat(self):
        print('狗吃骨头')

class Cat(Animal):
    def eat(self):
        print('猫吃鱼')

class Person(Animal):
    pass

def fun(object):
    object.eat()

# 开始调用函数

fun(Cat())
fun(Dog())
fun(Animal())
print('---------')
fun(Person())


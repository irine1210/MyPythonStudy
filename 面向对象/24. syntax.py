'''
@Author  : heyheyheyJoy
@Time    : 2022/1/30 4:11 下午
@File    : 24. syntax.py
'''

class Person(object):

    def __new__(cls, *args, **kwargs):
        print('__new__被调用执行，cls的id值为{0}'.format(id(cls)))
        obj = super().__new__(cls)
        print('创建的对象的id为{0}'.format(id(obj)))
        return obj

    def __init__(self,name,age):
        print('__init___被调用执行了，self的id为{0}'.format(id(self)))
        self.name = name
        self.age = age


print('object类对象的id为{0}'.format(id(object)))
print('Person这个类对象的id为{0}'.format(id(Person)))

p1 = Person('张三',20)
print('p1这个person类的实力对象的id为{0}'.format(id(p1)))

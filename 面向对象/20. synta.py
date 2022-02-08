'''
@Author  : heyheyheyJoy
@Time    : 2022/1/27 5:10 下午
@File    : 封装
'''

class Car:
    def __init__(self,brand):
        self.brand=brand
    def start(self):
        print("汽车已经启动～")

car = Car('宝马X5')
car.start()
print(car.brand)
print('-------------------------')

class Student:
    def __init__(self,name,age):
        self.name = name
        self.__age = age # 加两个__下滑线，表示不能在类的外部使用
    def show(self):
        print(self.name,self.__age)

stu_1 = Student('amy',20)
stu_1.show()

# 在类的外部调用name与age
#print(stu_1.__age)  # AttributeError: 'Student' object has no attribute '__age'
print(stu_1._Student__age)  # 20
print('-------------------------')


class Family:
    def __init__(self,name,age,job):
        self.name = name
        self.age = age
        self.job = job
    def show(self):
        print(self.name,self.age,self.job)

mother = Family('dear mom',30,'teacher')
father = Family('dear father',29,'boss')
sister = Family('dear sister',10,'student')

mother.show()
print(mother.age)


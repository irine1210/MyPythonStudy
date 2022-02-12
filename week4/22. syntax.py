'''
@Author  : heyheyheyJoy
@Time    : 2022/1/29 7:15 下午
@File    : 重写
'''

# 方法重写：如果子类对继承自父类的某个属性或方法不满意，可以在子类中对其进行重新编写
# 子类重写后的方法中可以通super().xxx()调用父类中被重写的方法

class Person(object):  #person继承了objet类,objet类是所有类的父类
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def info(self):
        print(self.name,self.age)

class Student(Person):  # Student继承了Person类
    def __init__(self,name,age,stu_no):
        super().__init__(name,age)  # 把父类的age和name传入
        self.stu_no = stu_no
    # ---------在Student里重写info---------
    def info(self):
        super().info()
        print(self.stu_no)

class Teacher(Person):
    def __init__(self,name,age,teach_of_year):
        super().__init__(name,age)
        self.teach_of_year = teach_of_year
     # ----------在Teacher里重写info---------
    def info(self):
        super().info()
        print(self.teach_of_year)


stu = Student('Amy',20,'1722')
teacher = Teacher('Joy',30,10)

stu.info()  # Amy 20
print('---------')
teacher.info()   # Joy 30

print('---------')
class Student:
    def __init__(self,name,age):
        self.name =  name
        self.age = age
    def __str__(self):
        return '我的名字是{0},今年{1}岁了'.format(self.name,self.age)
stu = Student('amy',20)
print(stu)  # 默认调用__str__()的方法
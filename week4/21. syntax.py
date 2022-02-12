'''
@Author  : heyheyheyJoy
@Time    : 2022/1/29 5:50 下午
@File    :继承
'''


class Person(object):  #person继承了objet类
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def info(self):
        print(self.name,self.age)

class Student(Person):  # Student继承了Person类
    def __init__(self,name,age,stu_no):
        super().__init__(name,age)  # 把父类的age和name传入
        self.stu_no = stu_no

class Teacher(Person):
    def __init__(self,name,age,teach_of_year):
        super().__init__(name,age)
        self.teach_of_year = teach_of_year

stu = Student('Amy',20,'1722')
teacher = Teacher('Joy',30,10)

# info()这个方法是从Person类里继承过来的,所以即使Student类里没有这个方法也可以调用
stu.info()  # Amy 20
teacher.info()   # Joy 30




'''
class A(object):
    pass

class B(object):
    pass

class C(A,B):   # C继承了A和B，有两个父类
    pass

'''

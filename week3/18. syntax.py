'''
@Author  : heyheyheyJoy
@Time    : 2022/1/26 8:47 下午
@File    : 18. syntax.py
'''


class Student:  # 类的规范：类名的首字母要大写，其余小写
    native_place='山西' # 直接写在类里面的变量成为类属性
    def __init__(self,name,age):
        self.name = name  # self.name 称为实例属性，进行了一个赋值操作，将局部变量的name值赋值给实体属性
        self.age = age

    # 实例方法
    def ear(self):  # 【类之内】的成为【方法】，类之外定义的成为函数 # 普通的方法，括号里面要写sef
        print('学生在吃饭')


    # 静态方法，括号里买呢不用写self
    @staticmethod
    def method():
        print('我使用了静态方法进行修饰，所以我是静态方法')

    # 类方法————要求传一个clss
    @classmethod
    def cm(cls):
        print('我使用了类方法')

print('------------类属性的使用方式-------------')
print(Student.native_place)

stu1 = Student('张三',30)
stu2 = Student('李四',40)

print(stu1.native_place)  #山西
print(stu2.native_place)   #山西

Student.native_place = '天津'
print(stu1.native_place)    #天津
print(stu2.native_place)    #天津


print('------------类方法的使用方式--------------')
Student.cm()

print('------------静态方法的使用方式-------------')
Student.method()
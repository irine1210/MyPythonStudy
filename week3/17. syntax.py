'''
@Author  : heyheyheyJoy
@Time    : 2022/1/26 8:03 下午
@File    : 17. syntax.py
'''


class Student:  # 类的规范：类名的首字母要大写，其余小写
    native_place='山西' # 直接写在类里面的变量成为类属性
    def __init__(self,name,age):
        self.name = name  # self.name 称为实例属性，进行了一个赋值操作，将局部变量的name值赋值给实体属性
        self.age = age

    def ear(self):  # 【类之内】的成为【方法】，类之外定义的成为函数 # 普通的方法，括号里面要写sef
        print('学生在吃饭')

    @staticmethod #静态方法，括号里买呢不用写self
    def method():
        print('我使用了静态方法进行修饰，所以我是静态方法')

    @classmethod # 类方法————要求传一个cls
    def hi(cls):
        print('我使用了类方法')

# 创建student类的对象
stu = Student('张三',20)  # stu叫做：根据Student类创建出来的实例对象
stu.ear() # 输出了：学生在吃饭
print(stu.age)
print(stu.name)

print('----------------')
Student.ear(stu)  #功能与  stu.ear() 相同
                 # stu 其实就是class中的self
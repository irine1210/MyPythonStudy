'''
@Author  : heyheyheyJoy
@Time    : 2022/1/26 9:09 下午
@File    : 19. syntax.py
'''

class Student:
    def __init__(self,name,age):  #  __init__ 初始化方法
        self.name = name
        self.age = age

    def eat(self):
        print(self.name+'在吃饭')


stu_1 = Student('张三',20)
stu_2 = Student('李四',30)
stu_1.eat() # 张三在吃饭

print('---------为stu2【动态绑定属性】------------')
stu_2.gender = '女' # 这是在创建完stu2属性之后又为它单独创建的属性，只对stu_2起作用
print(stu_1.name,stu_1.age) # 张三 20
print(stu_2.name,stu_2.age,stu_2.gender)  # 李四 30 女


print('---------为stu2【动态绑定方法】-----------')
# eat()方法是绑定在class对象中的
stu_1.eat() #  张三在吃饭
stu_2.eat() #李四在吃

# 定义在class之外的称为函数
def show():
    print('定义在class之外的称为函数')

stu_1.show = show  # 把show方法与stu_1 绑定
stu_1.show()   # 当与stu1绑定后，show就称之为方法



'''
@Author  : heyheyheyJoy
@Time    : 2022/1/20 8:49 下午
@File    : 9. syntax.py
'''

# 本节开始，学习元组成部分的内容

'''
# 可以变序列:字典、列表       不可变序列：字符串、元组
d = [10,20,30]
print(id(d)) # 4417905120

d.append(33)
print(id(d)) # 4417905120    增加元素后位置不变，说明【字典是可变序列】


s = 'hello'
print(id(s))  # 4498782512
s = s+'1worlddddddddd'
print(id(s))  #  4500084096   id变了，说明内存地址发生了变化


#列表是方括号[] 元组是小括号()

# 使用（）创建
d = ('python','world',98)
print(type(d))   # <class 'tuple'>  是tuple类型

# 使用内置函数 tuple((xx,xx,xx))创建  ----注意里面还有一个小括号，说明是元组元素
t1 = tuple(('hi','prpr',98))
print(t1)

t2 = ('hello')
print(type(t2))  # str

t3 = ('hello',)
print(type(t3))  # tuple  所以说如果元组里只有一个元素，那一定要加逗号
'''

t3=[]
t4=list()
print('空列表', t3, t4)

t5={}
t6=dict()
print('空字典', t5, t6)

# 空元组的创建方式
t1=()
t2=tuple()
print('空元组', t1, t2)

# 可以变序列:字典、列表       不可变序列：字符串、元组

# 2022/1/8

import math

print(ord('乘'))

import keyword
print(keyword.kwlist)

ww='hi'
print('类型',type(ww))
print('标示',id(ww))
print('值',ww)

ww='bobo'
print(ww)

name='张三'
age=8
print(type(name),type(age))
print('我叫'+name+'今年'+str(age))   # str与int类型链接时会报错，要报int转成str类型,使用str()转换即可
                                    # float与int也需要转换类型
a=10
b=198.8
c=False
print(type(a),type(b),type(c))

print(str(a),str(b),str(c),type(str(a)),type(str(b)),type(str(c)))


s=12.9999
print(s,int(s),type(int(s)))  #float转int会自动把小数部分省略


#s='12.9999'
#print(s,int(s),type(int(s)))  #浮点类型的str型不能转int。12.999 不行，但是 12就可以

'''   三引号代表多行注释
s=False
print(int(s),type(s)) #s必须为整数数字串
'''



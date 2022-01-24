'''
@Author  : heyheyheyJoy
@Time    : 2022/1/20 5:36 下午
@File    : 8. syntax.py
'''


# 字典元素的获取

score = {'amy':100,'joy':90}

''' 
#第一种方法：使用[] 
print(score['amy'])     # 100
print(score['pr'])    #  KeyError: 'pr' 表示要查的关键字不存在，会报错


# 第一种方法：使用 .get()方法 
print(score.get('amy'))   #  100
print(score.get('pr'))   #  None，不会报错，默认只是输出none
print(score.get('prpr',99))   #  99 --- 表示你规定了在查找指定的元素value不存在时，返回的默认值


# key的判断
print('prpr' in score) # Flase
print('prpr' not in score) # True


# 指定删除元素
del score['amy']
print(score)  # {'joy': 90} 会把一个键值对一起删除

score.clear()
print(score)   #  {} 清空字典的元素


#  增加
score['prpr'] = 98
print(score)   #  {'amy': 100, 'joy': 90, 'prpr': 98}

score['prpr'] = 100
print(score)   #   {'amy': 100, 'joy': 90, 'prpr': 100}  此时会覆盖成100
 

# 字典的常用操作  key()----获取关键字,  values()----获取值,  items()---获取value对

#获取所有的key
key = score.keys()
print(key)  # dict_keys(['amy', 'joy'])
print(list(key))  # ['amy', 'joy']  把字典类型转换成列表的类型

#获取所有的value
value = score.values()
print(value)   # dict_values([100, 90]) 记得加s
print(list(value))  # [100, 90] 把获取出来的value装到list里

# 获取所有的键值对

items = score.items()
print(items)  #  dict_items([('amy', 100), ('joy', 90)])  一个括号内部就是一个元组
print(list(items))  # [('amy', 100), ('joy', 90)]   转换之后是由一个个元组组成的


d = {'prpr':'nini','prprp':'nini'}  # d = {'key':'value'}  key 不能重复，value可以重复
print(d)   

'''
# 字典生成式
items = ['Fruit','Book','Milk']
prices = [98,87,80]

d = {item.upper():price for item,price in zip(items,prices)}
print(d)


# 以上部分，完成了【字典】的学习

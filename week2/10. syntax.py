'''
@Author  : heyheyheyJoy
@Time    : 2022/1/21 1:32 下午
@File    : 10. syntax.py
'''


# 整个t是一个元组，元组是不能直接添加元素的
# 而t[1] = [20,30]是列表，列表是可变序列，所以可用 .append() 函数来添加元素而 内存地址不变
# 也就是说，不能直接修改元组的内容，但是可以修改元组元素的内容-----有点类似广义表（？）

t = (90, [20, 30], 'hello')
print(type(t[1]))  # <class 'list'>

t[1].append(40)
print(t)  # (90, [20, 30, 40], 'hello')

# 元组的遍历
t = ('python','world',98)

print(t[0])   # python
# print(t[3])   # IndexError: tuple index out of range 元组下标超出了范围

t1 = ('python','world',98)
for item in t1:
    print(item)





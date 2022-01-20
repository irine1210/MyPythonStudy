'''
@Author  : heyheyheyJoy
@Time    : 2022/1/12 2:44 下午
@File    : 6. syntax.py



lst=[10,20,30,40,30,60]
lst.remove(30)
print(lst)    #  结果为：[10, 20, 40, 30, 60] 只会删除第一个30


# .pop()根据索引删除元素
lst2=[10,20,30,40,30,60]
lst2.pop(1) # 把一号位置上的元素删除
print(lst2)  #结果为 [10, 30, 40, 30, 60]

lst2.pop() #如果不写参数，默认删除最后一个（也就是栈顶元素啦）
print(lst2)  #结果为 [10, 30, 40, 30]


print('切片操作，删除至少一个元素，将产生一个新的列表对象\n')
lst=['hello','hi',23,50]
print('原列表为：',lst) # 原列表为： ['hello', 'hi', 23, 50]
new_lst=lst[1:3] #新列表为原列表的1，2位置元素
print('新列表为：',new_lst) # 新列表为：['hi', 23]


# 不产生新的列表，而是真正的删除
lst_2=['hello','hi',23,50]
lst_2[1:3]=[]  #用空列表把想要删除的位置替代即可
print(lst_2)   #['hello', 50]

# 清除列表中的所有元素
lst_3=['hello','hi',23,50]
print(lst_3.clear(),id(lst_3))  #None 4421278608


# del可直接将列表对象删除
del lst_3
print(lst_3,id(lst_3))  #报错： NameError: name 'lst_3' is not defined 已经完全删除了整个列表，所以定义都没了




# 排序  .sort()是对原列表进行操作，即操作前后id是不变的
lst=[20,40,10,2,30,12]
print('排序前的列表：',lst)  # 排序前的列表： [20, 40, 10, 2, 30, 12]
print(id(lst))  # 4311171552
lst.sort()  # 默认是升序

print('排序后的列表：',lst) # 排序后的列表： [2, 10, 12, 20, 30, 40]
print(id(lst)) # 4311171552 和原列表的id相同，说明是在同一个列表中进行更改的

lst.sort(reverse=True)  # 降序
print(lst)  #[40, 30, 20, 12, 10, 2]
print(id(lst))

lst.sort(reverse=False)  # 升序
print(lst)  # [2, 10, 12, 20, 30, 40]
print(id(lst))

# 排序  若调用内置sorted()函数进行排序，默认列表中所有元素从小到大排序，可以指定 reverse = True或reverse = False，原列表不变，而创建新的列表对象
lst=[20,40,10,2,30,12]
new_lst = sorted(lst)
print(lst,id(lst))  # [20, 40, 10, 2, 30, 12] 4481577440
print(new_lst,id(new_lst)) # [2, 10, 12, 20, 30, 40] 4481580000   id变了，说明调用sorted函数的话是开辟新空间来实现降序～

'''

# 列表生成式 [ f(i) for i in range(a,b) ]   f(i)是列表元素的表达式
lst =[i for i in range(1,10)]  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(lst)


lst1 =[i*i for i in range(1,10)]  # [1, 4, 9, 16, 25, 36, 49, 64, 81]
print(lst1)


lst2=[i for i in range(2,11,2)]
print(lst2)     # [2, 4, 6, 8, 10]


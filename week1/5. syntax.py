'''
@Author  : heyheyheyJoy
@Time    : 2022/1/11 4:01 下午
@File    : 5. syntax.py


print('输出三行四列的矩形')

for i in range(1,10):
    for j in range(1,i+1):
        print(i,'*',j,'=',i*j, end='\t')
    print()


for i in range(5):
    for j in range(1,11):
        if j%2==0:
            continue
        print(j,end='\t')
    print()


#创建列表的方式：使用[]
a = 10
list = ['hello','world','10']
print(id(list))
print(list)

#使用list()函数
list2=list(['hello','world','10','hello'])

print(list2[-4])

###### python中的list空间是动态分配的，直接用就行，不用担心多/不够用

print('使用index查找元素下标 ')
lst =['hello','world',98,'pp']

#print(lst.index('pp'))
#如果要查找的元素不存在，则：  ValueError: 'ppp' is not in list

print(lst.index('pp',1,4)) #在下标为1、2、3中查找hello


list=['hello','poop','kk',98]

print(list.index(98))
print(list[-1],list[-4])

# print(list[10]) # 超出范围 IndexError: list index out of range


# 列表的切片
ls=[10,20,30,40,50,60,70,80]
print(ls[1:6:1])  # [20, 30, 40, 50, 60]
print(ls[1:6:2])   # [20, 40, 60]
print(ls[6:1:-1])
print(ls[7:1:-1])



ls=[10,20,'hello']
print(99 not in ls)  #True
print('hello' in ls)  #False
'''

#增加列表元素 .append()
list=[100,200,300,'hello']
print(id(list))      # id=4374090208
list.append('hi')   # 结果为：[100, 200, 300, 'hello', 'hi']
print(list)
print(id(list))    # id=4374090208
                    #两次显示的id相同，说明是在同一个内存中进行了更改



'''
#在列表末尾至少增加一个元素  .extend()
list1=[100,200,300,'hello']
list2=[555,222,666,'hi']

list1.append(list2)
print(list1)    # 结果为： [100, 200, 300, 'hello', [555, 222, 666, 'hi']]
                # 把list2作为【一个】元素增加到表尾


list1_1=[100,200,300,'hello']
list2_2=[555,222,666,'hi']
list1_1.extend(list2_2)   #结果为： [100, 200, 300, 'hello', 555, 222, 666, 'hi']
print(list1_1)            #像末尾添加多个元素

#在任意位置添加一个元素 .insert()

list1=[100,200,300,'hello']
list1.insert(1,90) #在1的位置上加入90这个元素
print(list1)  #输出结果为  [100, 90, 200, 300, 'hello']




# 在任意位置添加N多个元素------切片
list_1 = [12,34,56,67,'hello']
list_2 = [222,333]
list_1[1:] = list_2   #把1到最后的位置的元素都切掉，把切掉的这些元素，换成list_2的元素
print(list_1)
'''

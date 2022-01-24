'''
@Author  : heyheyheyJoy
@Time    : 2022/1/23 7:47 下午
@File    : 13. syntax.py
'''


s = 'hello, python'
print(s.center(20,'%'))  # 居中对齐 %%%hello, python%%%%
print(s.ljust(20,'%'))  # 左顶格  hello, python%%%%%%%
print(s.ljust(10,'%'))  # 10的话就是默认   hello, python

print(s.zfill(20)) # 右对齐，使用0进行填充


s = 'hello my nanme is python'
lst = s.split()  # .split()方法按照空格去进行划分
print(lst)   #  ['hello', 'my', 'nanme', 'is', 'python']

s1 = 'hello*my*nanme*is*python'
lst2 = s.split(sep = '*')  # 以一个*作为划分
print(lst2)   # ['hello my nanme is python']

lst3=s1.split(sep='*', maxsplit = 1) #   maxsplit = k 表示最多分为k段
print(lst3)  # ['hello', 'my*nanme*is*python']

#  .rsplit() 表示从右侧开始劈分
lst4 = s1.rsplit(sep = '*',maxsplit=1)
print(lst4) #  ['hello*my*nanme*is', 'python']  只把右边第一个*分割出来的单词劈出来了

#------------ 合法的标示符：字母、数字、下划线  .identifer()进行判断 ------------

print('1. ','hello'.isidentifier())  # 1.  True 说明 hello是一个标示符
print('2. ','he++o'.isidentifier())  # 2.  False 说明 he++o不是标示符
print('3. ','张3_!'.isidentifier())   # 3.  False 带有！不是合法的标示符

#------------ 合法的字母： .isalpha()进行判断 ---------------
print('4. ','hello'.isalpha())  # 4.  True
print('5. ','hell999'.isalpha())  #5.  False

#------------ 合法的十进制数字： .isdecimal()进行判断 ------------
print('6. ','90'.isdecimal())   # 6.  True
print('7. ', '0100 0000'.isdecimal()) # 认为0100 0000 不是十进制数字


#------------ 判断是否是由字母和数字构成 .isalnum() ------------
print('8. ','hello333'.isalnum())  #  8.  True
print('9. ','hello++++333'.isalnum())   # 9.  False   'hello+++333'中有符号



s = 'hello,python'
print(s.replace('python','java')) # 用java代替python   # 输出结果：hello,java

s1 = 'hello,python,python,python'
print(s1.replace('python','java',2))  # 用java代替python，一共替换两次   # 输出结果：hello,java,java,python


a = 'hello,python'
a1=a[:5]  # 切到第五位位置
a2 = a[6:] # 从第六位开始往后切
print(a1) # hello
print(a2)  # python
print(a[1:5:2])  # 从1的位置切到5的位置（不包括5），步长为2
print(a[::2])  # hlopto 默认从0 开始，默认到最后一个元素
print(a[::-2])  # 负数的话，默认从最后一个元素开始到第一个字符串结束

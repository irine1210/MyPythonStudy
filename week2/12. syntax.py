'''
@Author  : heyheyheyJoy
@Time    : 2022/1/22 4:37 下午
@File    : 12. syntax.py
'''

a = 'he'
b = "he"

# 对相同的字符串只保留一份拷贝，不会开辟新的空间
print(a,id(a))  #he 4427446576
print(b,id(b))  #he 4427446576
print(c,id(c)) #he 4427446576

s='abadffer'
# print(s.index('h'))  # ValueError: substring not found 不存在h
print(s.index('a'))  # 0 因为a第一次出现的下标为0
print(s.rindex('a'))  # 2 因为a最后一次出现的位置为2

l = 'hello,hello'
print(l.index('lo'))  # 3 lo第一次出现的位置为3
print(l.find('lo'))  #3
print(l.rindex('lo')) # 9

# print(l.rindex('ff')) #  ValueError: substring not found
print(l.find('ff')) # -1  不会抛异常 所以用.find()进行字符串的查找比较好

k1 = 'AABBDDKSC'
k1.lower()
print(id(k1),id(k1))  # 转换前后的位置id是不同的，说明产生了新的字符对象


k2='heLLo,pyTHon'
print(k2) # heLLo,pyTHon
print(k2.title()) # Hello,Python  开头的字母变成大写了，其他都变为小写


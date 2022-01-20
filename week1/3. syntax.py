'''
a = int(input('输入第一个整数:'))  #此时的a和b是str类型
b = int(input('输入第二个整数:'))
c=a+b
#c = int(a)+int(b)  #必须要先转换成int才能进行相加的操作
print(c)


print('1. balabala')
print(bool(1))
print(bool('hello'))  # 空字符串是False



money=100
s=int(input('请输入取款金额:'))
if money>=s:
    money = money - s
    print('取款成功，余额为：',money)
else:
    print('钱不够啦')


a=int(input('输入一个整数：'))
if a%2==0:
    print('是偶数')
else:
    print('是基数')




score = int(input('请输入你的成绩：'))
if score>=90 and score<=100:
    print('you got A')
elif score<90 and score>=80:
    print('you got B')
elif score>=70 and score<=80:
    print('you got C')
elif score>=60 and score<=70:
    print('you got D')
else:
    print('输入错误成绩')




answer = input('您是会员吗:yes/no  \n')

if answer=='yes':
    print('您好，会员！')
    money=int(input('输入消费金额：'))

    if money>200:
        money=money*0.85
        print('折后金额为：',money)
    elif money>=100 and money<200:
        money=money*0.9
        print('折后金额为：', money)
    else:
        money=money*0.95
        print('折后金额为：', money)
else:
    print('您好，您不是会员')
    print('不打折')




num_a = int(input('请输入第一个整数：'))
num_b = int(input('请输入第二个整数：'))

if num_a > num_b:
    print(num_a ,'大于等于',num_b)
else:
    print(num_a ,'小于等于' ,num_b)


#使用条件表达式比较  if中为true，则输出if之前的，false则输出else之后的


num_a = int(input('请输入第一个整数：'))
num_b = int(input('请输入第二个整数：'))

print(str(num_a) +'大于等于'+str(num_b) if num_a>num_b  else  (str(num_a)+'小于等于'+str(num_b)))



#pass 的使用__没想好写什么内部代码，但为了保证程序不出错，可以写pass

answer = input('memer? yes/no')

if answer=='y':
    pass
else:
    pass



# range（）的使用方式
r = range(1,10)  #range（10）是从0到9，默认步长为1
print(list(r))  #list是列表的意思\\

r = range(1,10,2)  #range(start,stop,step)

print(10 in r) #输出结果为False，说明10 不在当前r的序列中；
print(9 in r) #输出结果为True，说明9不在当前r的序列中；

print(list(range(1,100,10)))
'''


a=1
while a<10:
    print(a)
    a+=1





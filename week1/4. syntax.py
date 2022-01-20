'''
@Author  : heyheyheyJoy
@Time    : 2022/1/10 2:16 下午
@File    : 4. syntax.py


a = 0
sum=0

while a<5:
    sum+=a
    a+=1

print('sum =',sum)


a=0
sum=0
while a<=100:
    a=a+1
    if(a%2==0):
        sum=sum+a

print('sum = ',sum)




for i in 'python':
    print(i)


for i in range(10):
    j=i*2
    print('第',i,'次打印',j)

i=0
sum=0
for i in range(101): #控制循环0——9次
    if i%2==0:
        sum=sum+i

print(sum)



print('输出100-999之间的水仙花数')
#153=3*3*3 + 5*5*5 + 1*1*1

for i in range(100,1000):
    ge = i%10
    shi = i//10%10
    bai = i//100   # 整除是双斜杠//

    if ge*ge*ge + shi*shi*shi + bai*bai*bai == i:
        print(i)


############### break的作用：直接结束全部循环，
print('从键盘录入密码，最多三次')

for i in range(3):
    pwd=int(input('请输入密码:'))
    if pwd == 999:
        print('密码正确')
        break
    else:
        print('密码不正确，请重新输入')


#############  continue的作用：continue后还有多少代码不管了，直接进入下一次循环！！！
print('输出1--50之间所有5的倍数')

for i in range(1,51):
    if i%5!=0:
        continue #直接下一次循环
    else:
        print(i)
'''

a=0
while a<3:
    pwd = input('请输入密码：')
    if pwd=='8888':
        print('yes')
        break
    else:
        a+=1
        print('No')
else:
    print('3次密码均错误')

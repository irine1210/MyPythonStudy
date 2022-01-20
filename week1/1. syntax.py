#2021/1/7

print('hello world') # 字符要加单引号

print(1+2)

#将数据输出到文件中。注意保存路径、使用file包
fp=open('/Users/peifengsun/PycharmProjects/feifei','a+') #如果文件存在就直接在文件后面追加内容
print('helllo joyy',file=fp)
fp.close()

print('hi','ppp')



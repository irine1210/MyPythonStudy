'''
@Author  : heyheyheyJoy
@Time    : 2022/2/10 3:03 下午
@File    : stu_system.py
'''

import os
filename = 'student.txt'

def main():
    while True:
        menu()  # 执行menu函数
        choice = int(input('请选择: '))
        if choice in [0, 1, 2, 3, 4, 5, 6, 7]:
            if choice == 0:
                answer = input('您确定退出系统吗？y/n')
                if answer == 'y' or answer == 'Y':
                    print('谢谢使用，再见!!')
                    break
                else:
                    continue
            elif choice == 1:
                insert()
            elif choice == 2:
                search()
            elif choice == 3:
                delete()
            elif choice == 4:
                modify()
            elif choice == 5:
                sort()
            elif choice == 6:
                total()
            elif choice ==7:
                show()
        else:
            print('选项有误，请重新输入！！')
            continue

def menu():
    print('============学生信息管理系统================')
    print('---------------功能菜单---------------')
    print('\t\t\t1. 录入学生信息')
    print('\t\t\t2. 查找学生信息')
    print('\t\t\t3. 删除学生信息')
    print('\t\t\t4. 修改学生信息')
    print('\t\t\t5. 排序')
    print('\t\t\t6. 统计学生总人数')
    print('\t\t\t7. 显示所有学生信息')
    print('\t\t\t0. 退出程序')
    print('-------------------------------------')

def insert():
    student_list = []
    while True:
        id = input('请输入id: ')
        if not id:
            break
        name = input('请输入姓名: ')
        if not name:
            break

        try:
            english = int(input('请输入英语成绩：'))
            python = int(input('请输入python成绩：'))
            java = int(input('请输入java成绩：'))
        except:
            print('输入无效，不是整数类型，请重新输入：')
            continue

        # 将录入的学生信息保存到字典中
        student = {'id': id, 'name': name, 'english': english, 'python': python, 'java': java}
        # 将(字典类型的)学生信息添加到列表中
        student_list.append(student)
        answer = input('是否继续添加？y/n\n')
        if answer == 'y':
            continue
        else:
            break

    # 调用save()函数将学生信息存储到文件中
    save(student_list)
    print('学生信息录入完毕')

def save(list):
    try:
        stu_txt = open(filename, 'a', encoding='utf-8')  # 打开文件，指定操作类型为 'a'（追加）
    except:
        stu_txt = open(filename, 'w', encoding='utf-8')  # 打开文件，指定操作类型为 'w'（写入）

    for item in list:
        stu_txt.write(str(item)+'\n')

    stu_txt.close()

def delete():
    #  =====所谓的删除，并不是真的'删除'，而是把不需要删除的重新写入！！===
    while True:
        student_id = input('请输入要删除的学生id: ')
        if student_id != '':
            if os.path.exists(filename):  # 如果磁盘中存在这个文件
                with open(filename,  'r', encoding='utf-8') as file:
                    student_old = file.readlines() # 把文件中的内容存到student_old这个变量里
            else:
                student_old = []

            flag = False  # 标记是否删除
            if student_old:  # 磁盘文件中有学生信息
                with open(filename, 'w', encoding='utf-8') as wfile:   # 'w'表示覆盖原文件内容
                    d = {}
                    for item in student_old:
                        d = dict(eval(item))  # 将字符串转成字典
                        if d['id'] != student_id:  # ！！！ID不相等的情况下，把他写入文件===这是删除的本质===！！
                            wfile.write(str(d)+'\n')
                        else:
                            flag = True
                    if flag:
                        print(f'学生id为{student_id}信息已被删除')
                    else:
                        print(f'没有找到学生id为{student_id}信息')
            else:
                print('无学生信息')  # 磁盘文件中无学生信息
                break

            show()  # 删除之后要重新选择学生信息
            answer = input('是否继续删除呢？y/n')
            if answer == 'y' :
                continue
            else:
                break
        else:
            print('输入内容不得为空!!!! ')
            break

def show():
    student_list = []
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            students = rfile.readlines()
            for items in students:
                student_list.append(eval(items))  # 将读取到的字符串转换为字典类型，再添加到student的列表中
            if student_list:
                show_student(student_list)
    else:
        print('暂未保存数据信息')

def modify():
    show()
    if os.path.exists(filename):  # 文件是否存在
        with open(filename, 'r', encoding='utf-8') as rfile:
            student_old = rfile.readlines()  # 此时读取到的是一系列的字符串
    else:
        return 0

    student_id = input('请输入要修改的学生id：')
    if student_id != '':
        with open(filename, 'w', encoding='utf-8') as wfile:
            for item in student_old:
                d = dict(eval(item))  # 把字符串类型转换为字典类型
                if d['id'] == student_id:
                    print('已找到学生信息，可以修改他的相关信息了！')
                    while True:
                        try:
                            d['name'] = input('请输入姓名：')
                            d['english'] = input('请输入该学生English成绩：')
                            d['python'] = input('请输入该学生python成绩：')
                            d['java'] = input('请输入该学生java成绩：')
                        except:
                            print('您的输入有误，请重新输入！！！')  # 会重新回到离他最近的 while True再次执行
                            continue
                        else:
                            break  # 没有出现异常的话，就退出当前的while True
                    wfile.write(str(d) + '\n')  # 把字典类型转换成str类型写入文件
                    print('修改成功！！！')
                else:
                    wfile.write(str(d)+'\n')  # 如果不是要修改的学生，就把原来的内容原封不动的写进去

        answer = input('是否要继续修改其他学生信息？y/n')
        if answer == 'y':
            modify()
    else:
        print('学生id不能为空')
        modify()

def search():
    student_query = []
    while True:
        id = ''
        name = ''
        if os.path.exists(filename):
            mode = input('按照ID查找请输入1，按照姓名查找请输入2： ')
            if mode == '1':
                id = input('请输入学生id： ')
            elif mode == '2':
                name = input('请输入学生姓名： ')
            else:
                print('请正确选择查找方式！！')
                search()
            with open(filename, 'r', encoding='utf-8') as rfile:
                student = rfile.readlines()
                for items in student:
                    d = dict(eval(items))
                    if id != '':
                        if d['id'] == id:
                            student_query.append(d)
                    elif name != '':
                        if d['name'] == name:
                            student_query.append(d)
                    else:
                        print('您输入的学生信息有误')
                # 显示查询结果
                show_student(student_query)
                # 清空列表
                student_query.clear()

                answer = input('还要继续查询吗？y/n')
                if answer == 'y':
                    continue
                else:
                    break
        else:
            print('暂未保存学生信息')

def show_student(list):
    if len(list) == 0:
        print('没有查询到学生信息，无数据显示')
        return 0
    else:
        # 定义标题格式
        format_title = '{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'
        print(format_title.format('ID', '姓名', '英语成绩', 'python成绩', 'java成绩', '总成绩'))
        # 定义内容的显示格式
        format_data = '{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'
        for items in list:
            print(format_data.format(items.get('id'),
                                     items.get('name'),
                                     items.get('english'),
                                     items.get('python'),
                                     items.get('java'),
                                     int(items.get('english'))+int(items.get('python'))+int(items.get('java'))))

def sort():
    #show()
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            student_list = rfile.readlines()  # 把str类型的信息先放到list里
           # print(f'student_list类型是 {type(student_list)}', print(student_list))
            student_new = []
            # print(f'student_new类型是 {type(student_new)}')

            for items in student_list:
                d = dict(eval(items))  # 转str类型为字典类型
                student_new.append(d)  # 把文件中str类型的学生信息转化为字典类型，再把每一条字典存到列表中

            # print(student_new)  # student_list列表里面的元素是str类型
                                  # student_new列表里面是字典类型。 解开看看就知道了

            choice = input('请选择次序 1.为升序  2.为降序：')
            if choice == '1':
                choice_bool = False
            elif choice == '2':
                choice_bool = True
            else:
                print('您的输入有误，请重新操作！')
                sort()

            mode = input('请选择排序方式：(1.按英语排序 2.按python排序 3.按java排序 4.按总成绩排序)  ')
            if mode == '1':
                student_new.sort(key=lambda x: int(x['english']), reverse=choice_bool)
            elif mode == '2':
                student_new.sort(key=lambda x: int(x['python']), reverse=choice_bool)
            elif mode == '3':
                student_new.sort(key=lambda x: int(x['java']), reverse=choice_bool)
            elif mode == '4':
                student_new.sort(key=lambda x: int(x['python'])+int(x['java'])+int(x['english']), reverse=choice_bool)
            else:
                print('您输入的信息有误')
                sort()
        show_student(student_new)

    else:
        print('文件不存在')
        return

def total():
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            students = rfile.readlines()  # 把读取的信息放到学生列表中
            if students:
                print(f'一共有{len(students)}名学生')
            else:
                print('还没有输入学生信息')
    else:
        print('还没有保存学生信息')


if __name__ == '__main__' :
    main()

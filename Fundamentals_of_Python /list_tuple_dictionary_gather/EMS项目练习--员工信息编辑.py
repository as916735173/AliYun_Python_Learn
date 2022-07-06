# 显示系统欢迎信息
print('-' * 20, '欢迎使用员工管理系统', '-' * 20)
# 创建一个列表，用来保存员工的信息，员工的信息已支付穿的行驶统一保存列表
emps = ['\t孙悟空\t18\t\t男\t\t花果山']
# 创建一个循环显示操作选项
while True:
    # 显示用户的选项
    print('请选择要做的操作：')
    print('\t\t\t1.查询员工')
    print('\t\t\t2.添加员工')
    print('\t\t\t3.删除员工')
    print('\t\t\t4.退出系统')
    user_choose = input('请选择[1-4]：')
    print('=' * 66)

    # 根据用户的选择做相关的操作
    if user_choose == '1':
        # 查询员工
        # 打印表头
        print('\t序号\t\t姓名\t\t年龄\t\t性别\t\t住址')
        # 创建一个变量来表示员工的序列号
        n = 1
        # 显示员工信息
        for emp in emps:
            print(f'\t{n}\t{emp}')
            n += 1
    elif user_choose == '2':
        # 添加员工
        # 获取要添加员工的信息，姓名、年龄、性别、住址
        emp_name = input('请输入员工的姓名：')
        emp_age = input('请输入员工的年龄：')
        emp_gender = input('请输入员工的性别：')
        emp_address = input('请输入员工的住址：')
        # 创建员工信息
        emp = f'\t{emp_name}\t{emp_age}\t{emp_gender}\t{emp_address}'
        # 显示提示信息
        print('以下员工将被添加到系统中')
        print('=' * 66)
        print('\t\t姓名\t\t年龄\t\t性别\t\t住址')
        print(emp)
        print('=' * 66)
        user_confirm = input('是否确认该操作[Y/N]：')
        # 将四个信息拼接为一个字符串，然后插入到列表中
        # 判断
        if user_confirm == 'y' or user_confirm == 'Y':
            # 确认
            emps.append(emp)
            # 显示提示信息
            print('添加成功')
        else:
            # 取消操作
            print('添加已取消')
            pass
    elif user_choose == '3':
        # 删除员工，根据员工的序号来删除员工
        # 获取要删除的员工的序号
        del_num = int(input('请输入要删除的员工的序号：'))
        # 判断序号是否有效
        if 0 < del_num <= len(emps):
            # 输入合法，根据序号来获取索引
            del_i = del_num - 1
            # 显示提示
            print('以下员工将被删除')
            print('=' * 66)
            print('\t序号\t\t姓名\t\t年龄\t\t性别\t\t住址')
            print(f'\t{del_num}\t{emps[del_i]}')
            print('=' * 66)
            user_confirm = input('该操作不可恢复，是否确认该操作[Y/N]：')
            # 判断
            if user_confirm == 'y' or user_confirm == 'Y':
                # 确认
                emps.pop(del_i)
                # 显示提示信息
                print('员工已被删除！')
            else:
                # 取消操作
                print('操作已取消！')
                pass
        else:
            # 输入有误
            print('您的输入有误，请重新操作！')
            pass
    elif user_choose == '4':
        # 退出系统
        print('欢迎使用，再见！')
        input('点击回车键退出！')
        break
    else:
        print('您的输入有误，请重新选择！')
        pass
    # 打印分割线
    print('=' * 66)

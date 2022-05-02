"""用户登录"""
import hashlib

import check_code


def login_by_username():
    check_code.checking()
    filename = 'users.txt'
    username = []
    active = 0

    import os  # 检测用户信息是否存在
    file_exist = os.path.exists(filename)
    if not file_exist:
        with open(filename, 'w'):
            print('暂无用户数据，请先注册！！！')
        quit()

    with open(filename, 'r') as file:
        names = file.read().splitlines()
        names = [name for name in names]
    while active == 0:
        usernameinput = input('请输入你的用户名：')
        userpasswordinput = input('请输入你的密码：')
        if (len(usernameinput.strip()) == 0) or (len(userpasswordinput.strip()) == 0):
            print('用户名或密码不为空,请重试！！！\n')
            continue
        for name_one in names:
            name_one = eval(name_one)
            username.append(name_one['username'])
        if usernameinput in username:
            for name_two in names:
                name_two = eval(name_two)
                if usernameinput == name_two['username']:
                    pws = name_two['salt'] + userpasswordinput
                    after_hash_password = hashlib.sha256(pws.encode("utf-8")).hexdigest()
                    if after_hash_password == name_two['password_hash']:
                        print('登录成功！！！')
                        active = 1
                        break
                    elif after_hash_password != name_two['password_hash']:
                        print('密码错误,请重试！！！\n')
                        break
        else:
            print('用户名不存在,请重试！！！\n')


def login_by_email():
    check_code.checking()
    filename = 'users.txt'
    email = []
    active = 0

    import os  # 检测用户信息是否存在
    file_exist = os.path.exists(filename)
    if not file_exist:
        with open(filename, 'w'):
            print('暂无用户数据，请先注册！！！')
        quit()

    with open(filename, 'r') as file:
        names = file.read().splitlines()
        names = [name for name in names]
    while active == 0:
        emailinput = input('请输入你的邮箱：')
        userpasswordinput = input('请输入你的密码：')
        if (len(emailinput.strip()) == 0) or (len(userpasswordinput.strip()) == 0):
            print('邮箱或密码不为空,请重试！！！\n')
            continue
        for name_one in names:
            name_one = eval(name_one)
            email.append(name_one['email'])
        if emailinput in email:
            for name_two in names:
                name_two = eval(name_two)
                if emailinput == name_two['email']:
                    pws = name_two['salt'] + userpasswordinput
                    after_hash_password = hashlib.sha256(pws.encode("utf-8")).hexdigest()
                    if after_hash_password == name_two['password_hash']:
                        print('登录成功！！！')
                        active = 1
                        break
                    elif after_hash_password != name_two['password_hash']:
                        print('密码错误,请重试！！！\n')
                        break
        else:
            print('邮箱不存在,请重试！！！\n')


def login_way():
    activekey_login = 0
    while activekey_login == 0:
        login_way = input('用户名还是邮箱登录?\n(键入"用户名"或"邮箱"以继续...)\n(键入"取消"以取消操作...)\n')
        if login_way == '用户名':
            login_by_username()
            activekey_login = 1
        elif login_way == '邮箱':
            login_by_email()
            activekey_login = 1
        elif login_way == '取消':
            activekey_login = 1
        else:
            print('请不要键入除"用户名"或"邮箱"以外的字符！！！\n')

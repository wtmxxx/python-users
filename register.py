"""用户注册"""
import json
# 加密密码函数
import hashlib
import random
import string

import check_code

def addsalt():
    active = 0
    #激活while时使用
    salts = ''
    #先建一个空白字符串
    while active < 10:
        #用while循环随机生成一个6位数验证码
        salt_one = random.choice(string.digits)
        salt_two = random.choice(string.ascii_letters)
        salt = salt_one + salt_two
        #随机生成一个0~9的数字
        salts += salt
        active += 1
    return salts

before_salt = addsalt()


def secret(password):
    pws = before_salt + password
    after_password = hashlib.sha256(pws.encode("utf-8")).hexdigest()
    return after_password


def register():
    """用户注册"""

    email = check_code.checking()
    print(f'验证邮箱{email}将成为注册邮箱')
    filename = 'users.txt'
    users = {}
    namecheck = []

    import os #检测用户信息是否存在
    file_exist = os.path.exists(filename)
    if not file_exist:
        with open(filename, 'w'):
            print('你是第一个注册的用户！！！')


    with open(filename, 'r+') as file:
        names = file.read().splitlines()
        for name in names:
            name = eval(name)
            namecheck.append(name['username'])
        namecheck = [name.lower() for name in namecheck]
        while True:
            username = input('请输入您要注册的用户名：')
            if username.lower() in namecheck:
                print('用户名已存在,请重试！！！')
                continue
            elif len(username.strip()) == 0:
                print('用户名不为空！！！')
                continue
            users['username'] = username
            users['email'] = str(email)
            password = input('请输入密码：')
            users['password'] = password #如果不想显示出用户的真实密码可以把这行代码删除
            users['password_hash'] = secret(password)
            users['salt'] = before_salt

            # 加密密码

            users = json.dumps(users, ensure_ascii=False)
            users += f'\n'
            file.write(users)
            print(f'注册成功！！！\n您的邮箱为：{email}\n您的用户名为：{username}\n您的密码为：{password}')
            break
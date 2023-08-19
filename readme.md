滴滴滴，[沃特陌](https://www.wotemo.com/)与您汇报情况

历经几个周末的时间，我终于将这款**用户注册与登录系统**做出来啦~撒花✿✿ヽ(°▽°)ノ✿

### 一.特性

 1. 邮箱验证码验证身份的**真实性**
 2. 验证码错误次数**限制**
 3. 验证码具有**时效性**，超时将会失效（这里设置的是五分钟）
 4. 可以用'**用户名**'或者'**邮箱**'登录，登录方式不再单一
 5. 使用**哈希函数**进行加密，用户信息更安全
 6. 多用**if**等简单语句，小白也能看懂

### 二.基础要求

 1. Python的基本语法
 2. 熟练掌握**if**，**else**，**while**，**for**等语句
 3. 会使用**def**函数
 4. 会**调用模块**（import module）
 5. 了解**哈希函数**
 6. 了解**列表**，**字典**的格式与用法
 7. 会使用**open**等语句读写txt文件以存储用户数据
 8. 用到的模块有：**json**，**hashlib**，**random**，**string**，**os**，**time**等

### 三.代码部分
#### 本系统由四部分代码组成：

 1. **users.py**（主代码，程序在此运行）
 2. **login.py**（用户登录时调用）
 3. **register.py**（用户注册时调用）
 4. **check_code.py**（发送验证码时调用）

#### 第一部分：uers.py
```python
"""用户选择登录或注册，这是主代码，在这里运行程序"""
# 本代码由沃特陌Wotemo自主编写
import register
import login
activekey = 0
while activekey == 0:
    choice = input('你想登录还是注册？\n(键入"注册"或"登录"以继续...)\n(键入"取消"以取消操作...)\n')
    if choice == '注册':
       register.register()
       activekey = 1
    elif choice == '登录':
        login.login_way()
        activekey = 1
    elif choice == '取消':
        activekey = 1
    else:
        print('请不要键入除"注册"或"登录"以外的字符！！！\n')
```
#### 第二部分：login.py
```python
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
```
#### 第三部分：register.py
```python
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
```
#### 第四部分：check_code.py
```python
"""验证码的发送与验证"""
def checking():
    import random
    # 调用random函数随机生成验证码
    to_addr_input = input(f'我们需要验证您身份的真实性\n请输入您的邮箱,以接收验证码：\n')
    check_times = 0
    while (to_addr_input.find("@") == -1 or to_addr_input.find(".") == -1):
        if (check_times >= 2):
            print('您的错误次数过多，请稍后重试...')
            quit()
        print("错误的邮箱格式")
        to_addr_input = input("请输入您的邮箱以接收验证码：\n")
        check_times += 1

    def check_code():
        active = 0
        # 激活while时使用
        codes = ''
        # 先建一个空白字符串
        while active < 6:
            # 用while循环随机生成一个6位数验证码
            code = str(random.randint(0, 9))
            # 随机生成一个0~9的数字
            codes += code
            active += 1
        return codes

    check_codes = check_code()

    def send_code():
        # smtplib 用于邮件的发信动作
        import smtplib
        # email 用于构建邮件内容
        from email.mime.text import MIMEText
        # 构建邮件头
        from email.header import Header
        # 发信方的信息：发信邮箱，QQ 邮箱授权码
        from_addr = '此处填写你的发件邮箱，用作发送验证码，例：wotemo@qq.com'
        password = '此处填写你的smtp密钥，例：edghkejyddhjsoid (在QQ邮箱网站中获取)'
        # 收信方邮箱
        to_addr = to_addr_input
        # 发信服务器
        smtp_server = 'smtp.qq.com'
        # 邮箱正文内容，第一个参数为内容，第二个参数为格式(plain 为纯文本)，第三个参数为编码
        msg = MIMEText(f'【沃特陌】您正在进行登录/注册操作，您的验证码为：{check_codes}，请在10分钟内按页面提示完成验证，切勿将验证码泄露给他人。', 'plain', 'utf-8')
        msg['From'] = Header('沃特陌')
        msg['To'] = Header('用户')
        msg['Subject'] = Header('沃特陌邮箱验证码')
        server = smtplib.SMTP_SSL(smtp_server)
        server.connect(smtp_server, 465)
        server.login(from_addr, password)
        server.sendmail(from_addr, to_addr, msg.as_string())
        # 关闭服务器
        server.quit()

    try:
        send_code()
        print('验证码已发送到您的邮箱中，请注意查收...')
        import time #开启计时器，验证码过时失效
        time_start = time.time()

    except:
        print('验证码发送失败，请稍后重试，或反馈客服wotemo@qq.com')
        quit()

    check_code_input = input('请输入您的验证码：')
    time_end = time.time()
    time_continue = time_end - time_start
    check_times = 0
    while True:
        if (time_continue > 300):
            print('验证码超时，请稍后重试...')
            quit()
        if (check_times >= 2):
            print('您的错误次数过多，请稍后重试...')
            quit()
        if (str(check_code_input) == str(check_codes)):
            print('验证通过，请继续您的操作...')
            break
        else:
            print('验证码错误，请重试...')
            check_code_input = input('请输入您的验证码：')
            check_times += 1
    return to_addr_input
```

### 四.系统使用
 1. 将**check_code.py**中的第**38**,**39**行代码改为你自己的邮箱和密钥![check_code部分代码](https://img-blog.csdnimg.cn/7f05baca871044919f7a5f16d48e5656.png)
 2. 在**users.py**中运行程序，按照提示进行操作即可
 3. 如果不想显示明文密码，可将register.py中的第67行代码注释掉![register部分代码](https://img-blog.csdnimg.cn/3057e873ded0411a9842a6b8101b1c69.png)
### 五.进程展示
 1.**用户注册**展示
![进程展示--注册](https://img-blog.csdnimg.cn/59d4f5291f8143dc9fe1e2481fd1ca3b.png)
 2.**用户登录**展示
![进程展示--登录](https://img-blog.csdnimg.cn/70ca96e8348e4712998fa93bc6df5cf9.png)
 3.**邮箱验证码**展示
 ![进程展示--验证码](https://img-blog.csdnimg.cn/88c66ef81d9d49bc8cb9ba0e8a1a6d46.png)

### 六.代码获取
 1. [Github](https://github.com/wtmxxx/users)：https://github.com/wtmxxx/users

### 七.联系方式
 1. [我的博客](https://www.wotemo.com/)：https://www.wotemo.com/
 2. QQ：保密
 3. 邮箱：保密
 4. [Github](https://github.com/wotemo/)：https://github.com/wtmxxx/

本代码由**沃特陌**（[Wotemo](https://www.wotemo.com/)）自主编写，如有瑕疵可以和我反映哦~
如果有不懂的地方也可以和我交流哟(＾Ｕ＾)ノ~ＹＯ

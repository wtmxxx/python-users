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
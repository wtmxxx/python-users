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

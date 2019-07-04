#创建一个管理账号密码的数据库
users = {'baihuanyu':'x2323111','qianduoduo':'imadog','kitty':'imacat'}
def user_name(user_name,password):
    '''定义一个用户函数'''
     # .keys()表示字典的键
     # users【】 表示字典的值
    if user_name in users.keys():
        if password == users[user_name]:
            print('登陆成功')
        else :
            print('密码错误')
    else :
        print('该用户尚未注册')
        # 把新的键值对放入数据库
        users[user_name] = password
        print('恭喜你成为我们的新会员')
user_name('baihuan','1')
print(users)
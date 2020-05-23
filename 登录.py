
f=open('user_data_file.txt','r',encoding='UTF-8')
f1=open('user_data_file.txt','w',encoding='UTF-8')
user_data={}
user_data.update(f)
for (key,value) in user_data.items():
    f1.write('%s:%s\n' % (key, value))
def new_user():
    prompt="请输入用户名:"
    while True:
        name=input(prompt)
        if name in user_data:
            prompt='此用户名已被使用,请重新输入:'
            continue
        else:
            break
    passwd=input('请输入密码:')
    if len(passwd) <8:
        print("您的密码长度小于8!")
        print('注册不成功!请重新输入!')
    else:
        user_data[name]=passwd
        print('注册成功')
def old_user():
    prompt='请输入用户名:'
    while True:
        name = input(prompt)
        if name not in user_data:
            prompt=('你输入的用户名不存在，请重新输入:')
            continue
        else:
            break
    passwd=input('请输入密码:')
    pwd=user_data.get(name)
    if passwd==pwd:
        print('欢迎进入Web开发站!')
    else:
        print("密码错误!")
def 数据库管理():
    print(user_data)
def showmenu():
    prompt='''
    --- 新建用户:N/n ---
    --- 登录用户:E/e ---
    --- 退出用户:Q/q ---
    --- 查看数据库:T/F ---
    --- 请输入指令: '''
    while True:
        chosen=False
        while not chosen:
            choice = input(prompt)
            if choice not in 'NnEeQqTF':
                print('您输入的指令有误!,请重新输入:')
            else:
                chosen=True
        if choice == 'q' or choice == 'Q':
            print('--- 再见,欢迎下次再来! ---')
            f.close()
            f1.close()

            break
        if choice == 'n' or choice == 'N':
            new_user()
        if choice == 'e' or choice == 'E':
            old_user()
        if choice == 'T' or choice == 'F':
            数据库管理() 
if __name__=='__main__':
    showmenu()




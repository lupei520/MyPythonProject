def 猜随机数字游戏():
    import random
    try:
        secret=random.randint(1,10)
        print('-------卢沛狗专业实验室-------')
        temp=input('请猜一下卢沛狗博士心中的数字:')
        guess=int(temp)
        while guess!=secret:
            temp=input('哎呀,你猜错了，请重新输入:')
            guess=int(temp)
            if guess==secret:
                print('卧槽,你是卢沛狗心里的蛔虫吗,你怎么可能会知道呢?')
                print('奖励请查看游戏奖励.txt这个文件!')
                f=open('游戏奖励.txt','w')
                f.write('推销一波:请来到卢沛狗的网站:http://192.168.0.109\n文件分享:ftp://192.168.0.109\nQQ群:864610016')
                f.close()
            else:
                if guess>secret:
                    print('数字大了!')
                else:
                    print('数字小了!')
    except TypeError as r:
        print('程序出错了QAQ,错误原因是:你输入的东西不是整形数字,而是其他东西，类型不一样!')
        print('系统版原因:'+str(r))
    except ValueError as r:
        print('程序出错了QAQ,错误原因是:你输入的东西不是整形数字,而是其他东西，类型不一样!')
        print('系统版原因:'+str(r))
    except SyntaxError:
        print('该错误和用户输入无关,这是程序员输入出BUG了,请及时通知!')
    finally:
        print('游戏结束不玩了!')
if __name__=='__main__':
    猜随机数字游戏()


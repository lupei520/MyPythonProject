import random
import time
def 秘籍版():
 超级幸运值=random.randint(1000,10000)
 if year==秘籍:
     print("你的幸运值为",超级幸运值)
     print("你的总评分为SSS++++,你是全世界最幸运的人!!!!")
秘籍="卢沛轩最帅"
year=input("请输入秘籍来提升你的幸运值:")
def 普通版():
 幸运值=random.randint(-250,250)
 print("你的幸运值为:",幸运值)
 if 幸运值<=-150:
     print("你的总评分为D!")
     print("你好倒霉啊!你的级别为非酋！！！！你打游戏100%抽不中SSR！")
 elif -150<幸运值<=-100:
     print("你的总评分为C!")
     print("你还是比较倒霉的！")
 elif -100<幸运值<=0:
     print("你的总评分为B")
     print("你的幸运值比较平衡,不好也不坏!")
 elif 0<幸运值<250:
     print('你的总评分为A')
     print('你还是比较幸运滴!')
 elif 幸运值==250:
     print("你的总评分为S")
     print("你真的非常非常幸运!")
if year==秘籍:
    print("你输入的秘籍是正确的，已为你提升幸运值!")
    time.sleep(3)
    秘籍版()
else:
    print("你输入的秘籍是错误的!所以你没有提升幸运值!")
    time.sleep(3)
    普通版()




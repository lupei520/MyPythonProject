English={'乌龟':'tortoise','恐龙':'dinosaur','猫':'cat','狗':'dog'}
English2={'袋鼠':'kangaroo',"老鼠":"mouse","狮子":"lion","宇宙":"universe"}
English3={"国家":'country',"老虎":'tiger',"鸵鸟":"ostrich","屎":"shit","我(主格)":"I","你(主格)":"you","他":"he","她":"she","他们":"they"}
print ("所有单词都必须一次全部答对，否则，你永远都出不去!!!!!")
while True:
    a=input('乌龟: ')
    b=input('恐龙: ')
    c=input("猫: ")
    d=input("狗: ")
    if a==English['乌龟'] and b==English["恐龙"] and c==English['猫'] and d==English["狗"]:
        print ("你答对了,但是这仅仅连热身都算不上!!!!")
        break
while True:
 e=input('袋鼠: ')
 f=input('老鼠: ')
 g=input('狮子: ')
 h=input('宇宙: ')
 if e==English2['袋鼠'] and f==English2["老鼠"] and g==English2['狮子'] and h==English2["宇宙"]:
     print ("给你休息一下，切记，这是魔鬼训练!!!!")
     break
while True:
    i=input('国家:')
    j=input('老虎:')
    k=input('鸵鸟:')
    l=input('屎:')
    m=input('我(主格(大写)):')
    n=input('你(主格):')
    o=input('他(主格):')
    p=input('她(主格):')
    q=input('他们(主格):')
    if i==English3['国家'] and j==English3['老虎'] and k==English3['鸵鸟'] and l==English3['屎'] and m==English3['我(主格)'] and n==English3['你(主格)'] and o==English3['他'] and p==English3['她'] and q==English3['他们']:
        print("你热身成功了!!!")
        break
    else:
        print("你答错了，请输入正确答案，否则你永远出不去这个程序!!!!")

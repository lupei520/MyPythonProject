one=[]
for x in range(201):
    one.append(x*x)
two=one[:101]
one.reverse()
two.reverse()
if one[0]/two[0]==4: 
    print("成功了！")
    print("one列表的第0个元素的值是:",one[0])
    print("two列表的第0个元素的值是:",two[0])
    print('它们相除等于:',one[0]/two[0])
    print("所以成功!")
else:
    print("失败了！")
    print("one列表的第0个元素的值是:",one[0])
    print("two列表的第0个元素的值是:",two[0])
    print('它们相除等于:',one[0]/two[0])
    print("所以不成功!")
    if one[0]!=40000:
        print("请检查第二行，第五行和第七行的代码!")
    elif two[0]!=10000:
        print("请检查第四行，第六行和第七行的代码")
    else:
        print("如果你看到了这条消息，说明你是在乱搞!，请重新编写这个程序!")
        

import time
def power(x,y):
    if y:          #判断y是否为True，如果为True，则执行下面代码！
        return x*power(x,y-1)        #没调用一次power函数，y的值就会减少一，知道为0，不为True!
    else:
        return 1
number=int(input("请输入一个正整数作为X:"))
number2=int(input("请输入一个正整数作为X的几次方:"))
shit=power(number,number2)
if __name__=="__main__":
 print("%d的%d次方是%d" %(number,number2,shit))
 time.sleep(2)
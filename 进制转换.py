import time
def two_change_ten():
    two=input('请输入你的二进制数值:')
    two=int('0b'+two,2)
    print(two)
    time.sleep(10)
def ten_change_two():
    num=int(input('请输入你的十进制数:'))
    num=bin(num)
    print(num)
    time.sleep(10)
def ten_change_16():
    num=int(input('请输入你要转成十六进制的数:'))
    num=hex(num)
    print(num)
    time.sleep(10)
def ten_change_8():
    num=int(input('请输入你要转成八进制的数:'))
    num=oct(num)
    print(num)
    time.sleep(10)
def eight_change_10():
    num=input('请输入八进制数:')
    num=int('0o'+num,8)
    print(num)
    time.sleep(10)
def sixteen_change_10():
    num=input('请输入十六进制数:')
    num=int('0x'+num,16)
    print(num)
    time.sleep(10)
Hello=input("你需要二转十(1),还是十转二(2),还是十转十六(3),还是十转八(4),还是八转十(5),还是十六转十(6):")
if Hello=='二转十' or Hello=='1':
    two_change_ten()
if Hello=='十转二' or Hello=='2':
    ten_change_two()
if Hello=='十转十六' or Hello=='3':
    ten_change_16()
if Hello=='十转八' or Hello=='4':
    ten_change_8()
if Hello=='八转十' or Hello=='5':
    eight_change_10()
if Hello=='十六转十' or Hello=='6':
    sixteen_change_10()
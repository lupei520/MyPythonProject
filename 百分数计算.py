import decimal
class Percentage_calculation:
    def open_calculation(self):
        import time
        self.a=decimal.Decimal(input('请输入原价:'))
        self.b=input('请输入百分率:')
        if '%' in self.b:
            self.b=self.b.strip('%')
            self.b=decimal.Decimal(self.b)
            self.b=self.b/100
        else:
            self.b=decimal.Decimal(self.b)
        print('结果:',self.a*self.b)
        print('四舍五入的结果:',round(self.a*self.b))
        time.sleep(10)
    def remember(self):
        import time
        self.a=decimal.Decimal(input('请输入原价:'))
        self.b=input('请输入百分率:')
        self.c=decimal.Decimal(input('请输入存期:'))
        if '%' in self.b:
            self.b=self.b.strip('%')
            if type(self.b) == float or type(self.b) != int:
                self.b=decimal.Decimal(self.b)
            else:
                print('......输入有误!......')
            self.b=decimal.Decimal(self.b)
            self.b=self.b/100
        else:
            self.b=decimal.Decimal(self.b)
        print('你得到的利息是:',self.a*self.b*self.c)
        print('你得到的本金是:',self.a*self.b*self.c+self.a)
        print('为了精准,使用四舍五入计算利息:',round(self.a*self.b*self.c))
        print('为了精准,使用四舍五入计算利息:',round(self.a*self.b*self.c+self.a))
        time.sleep(10)
test=Percentage_calculation()
name=input('请问你需要的是直接计算(1),还是计算利息(2):')
if name=='直接计算' or name=='1':
    test.open_calculation()
if name=='计算利息' or name=='利息' or name=='2':
    test.remember()
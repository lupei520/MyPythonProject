class Rectangle:
    long=5
    wldth=4
    def getRect(self):
        print('.......正在为你展示矩形的长和宽.......')
        print('这个矩形的长是:%.2f'% self.long ,'宽是:%.2f' % self.wldth)
    def setRect(self):
        print('.......请你说出这个矩形的长和宽.......')
        self.long=float(input('长:'))
        self.wldth=float(input('宽:'))
    def getArea(self):
        print('.......正在计算面积.......')
        print(self.long*self.wldth)
    def getPerimeter(self):
        print('.......正在计算周长.......')
        print((self.long+self.wldth)*2)
rect=Rectangle()
rect.setRect()
rect.getRect()
rect.getArea()
rect.getPerimeter()

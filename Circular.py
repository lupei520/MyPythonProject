class Circular:
    from decimal import Decimal
    import math
    def __init__(self,r=None,d=None,π='3.14',area=None,circumference=None):
        self.r=r
        self.d=d
        self.π=self.Decimal(π)
        self.area=area
        self.circumference=circumference
    def Area(self):
        if self.r!=None:
            self.r=str(self.r)
            self.r=self.Decimal(self.r)
            self.area=self.r*self.r*self.π     #面积等于半径*半径*3.14
            print(self.r,'*',self.r,'*',self.π,'=',self.area)
            return self.area
        elif self.d!=None and self.r==None:
            self.r=str(self.d/2)
            self.r=self.Decimal(self.r)
            self.area=self.r*self.r*self.π
            print(self.r,'*',self.r,'*',self.π,'=',self.area)
            return self.area
    def Circumference(self):
        if self.d==None and self.r!=None:       #判断d是否有值
            self.r=str(self.r)
            self.r=self.Decimal(self.r)
            self.d=self.r/2
        elif self.d!=None:      #判断d是否有值
            self.d=str(self.d)
            self.d=self.Decimal(self.d)
        def count(d=self.d,π=self.π):     #创建一个闭包函数，用来计算结果(上面的步骤用于将半径转化为直径，下面的步骤为直径x3.14)
            self.circumference=d*self.π
            print(d,'*',π,'=',self.circumference)
            return d,'*',π,'=',self.circumference
        count()
    def Radius(self):
        if self.d!=None:
            self.d=str(self.d)
            self.d=self.Decimal(self.d)
            self.r=self.d/2
        elif self.area!=None:
            self.area=str(self.area)
            self.area=self.Decimal(self.area)
            self.r=self.area/self.π
            self.r=self.math.sqrt(self.r)
        elif self.circumference!=None:
            self.circumference=str(self.circumference)
            self.circumference=self.Decimal(self.circumference)
            self.r=self.circumference/self.π/2
        print(self.r)
if __name__ == '__main__':
    test=Circular(circumference=18.84)
    test.Radius()
     
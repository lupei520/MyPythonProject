class parallelogram:
    import time
    def __init__(self):
        self.ask=input("请问你是要计算面积还是周长,还是全都要:")
        if self.ask == '面积' or self.ask == '计算面积' or self.ask=='1':
            self.length_h=float(input("请输入图形的高:"))
            self.length_a=float(input("请输入图形的底:"))
            if big_ask=="三角形":
                self.length_d=float(input('请输入C的长度:'))
        if self.ask == '周长' or self.ask=='计算周长' or self.ask=='2':
            self.length_c=float(input('请输入a的边长:'))
            self.length_b=float(input('请输入b的边长:'))
            if big_ask=="三角形":
                self.length_d=float(input('请输入C的长度:'))
        if self.ask=='我全都要' or self.ask=="3":
            self.length_h=float(input("请输入图形的高:"))
            self.length_a=float(input("请输入图形的底:"))
            self.length_c=float(input('请输入a的边长:'))
            self.length_b=float(input('请输入b的边长:'))
            if big_ask=="三角形":
                self.length_d=float(input('请输入C的长度:'))
    def area_get(self):
        print("他的面积为:",self.length_a*self.length_h)
        self.time.sleep(10)
    def circumference(self):
        print("他的周长为:",2*(self.length_c+self.length_b))
        self.time.sleep(10)
class delta(parallelogram):
    def area_get(self):
        print('他的面积为:',self.length_a*self.length_h/2)
        self.time.sleep(10)
    def circumference(self):
        print('他的周长为:',self.length_c+self.length_b+self.length_d)
        self.time.sleep(10)
big_ask=input('请输入你要计算的图形:')
if big_ask=='平行四边形':
    test=parallelogram()
    if test.ask == '面积' or test.ask == '计算面积' or test.ask=='1':
        test.area_get()
    if test.ask == '周长' or test.ask=='计算周长' or test.ask=='2':
        test.circumference()
    if test.ask=='我全都要' or test.ask=="3":
        test.area_get()
        test.circumference()
if big_ask=='三角形':
    test2=delta()
    if test2.ask == '面积' or test2.ask == '计算面积' or test2.ask=='1':
        test2.area_get()
    if test2.ask == '周长' or test2.ask=='计算周长' or test2.ask=='2':
        test2.circumference()
    if test2.ask=='我全都要' or test2.ask=="3":
        test2.area_get()
        test2.circumference()





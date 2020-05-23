class axe:
    import time
    from fractions import Fraction
    def Hello(self):
        self.one,self.two=input('请输入需要解开的比例:').split('=')
        self.a,self.b=self.one.split(':')
        self.c,self.d=self.two.split(':')
        if self.a=='X' or self.a=='x' or self.a=='y' or self.a=='Y' or self.a=='a' or self.a=='A' or self.a=='z' or self.a=='Z':
            self.b=float(self.b)
            self.c=float(self.c)
            self.d=float(self.d)
            self.important=float(self.b*self.c)
            self.a=float(self.important/self.d)
            print('X等于:',self.a)
        elif self.b=='x' or self.b=='X' or self.b=='y' or self.b=='Y' or self.b=='a' or self.b=='A' or self.b=='z' or self.b=='Z':
            self.a=float(self.a)
            self.c=float(self.c)
            self.d=float(self.d)
            self.important=float(self.a*self.d)
            self.b=float(self.important/self.c)
            print('X等于:',self.b)
        elif self.c=='x' or self.c=='X' or self.c=='y' or self.c=='Y' or self.c=='a' or self.c=='A' or self.c=='z' or self.c=='Z':
            self.a=float(self.a)
            self.b=float(self.b)
            self.d=float(self.d)
            self.important=float(self.a*self.d)
            self.c=float(self.important/self.b)
            print('X等于:',self.c)
        elif self.d=='x' or self.d=='X' or self.d=='y' or self.d=='Y' or self.d=='a' or self.d=='A' or self.d=='z' or self.d=='Z':
            self.a=float(self.a)
            self.b=float(self.b)
            self.c=float(self.c)
            self.important=float(self.b*self.c)
            self.d=float(self.important/self.a)
            print('X等于:',self.d)
        self.time.sleep(10)
    def fenshu(self):
        from fractions import Fraction
        super_big_ask=input('a:b=c:d中谁是x:')
        if super_big_ask=='a':
            self.one=input('请输入b的值:')
            if '/' not in self.one:
                self.b=float(self.one)
            elif '/' in self.one:
                self.b_1,self.b_2=self.one.split('/')
                self.b_1=int(self.b_1)
                self.b_2=int(self.b_2)
                self.b=Fraction(self.b_1,self.b_2)
            self.one=input('请输入c的值:')
            if '/' not in self.one:
                self.c=float(self.one)
            elif '/' in self.one:
                self.c1,self.c2=self.one.split('/')
                self.c1,self.c2=int(self.c1),int(self.c2)
                self.c=Fraction(self.c1,self.c2)
            self.one=input('请输入d的值:')
            if '/' not in self.one:
                self.d=float(self.one)
            elif '/' in self.one:
                self.d1,self.d2=self.one.split('/')
                self.d1,self.d2=int(self.d1),int(self.d2)
                self.d=Fraction(self.d1,self.d2)
            self.important=self.b*self.c
            self.a=self.important/self.d
            print('X等于(小数形式):',self.a)
            self.a=str(self.important/self.d)
            print('X等于(分数形式):',Fraction(self.a))
        if super_big_ask=='b':
            self.one=input('请输入a的值:')
            if '/' not in self.one:
                self.a=float(self.one)
            elif '/' in self.one:
                self.a1,self.a2=self.one.split('/')
                self.a1,self.a2=int(self.a1),int(self.a2)
                self.a=Fraction(self.a1,self.a2)
            self.one=input('请输入c的值:')
            if '/' not in self.one:
                self.c=float(self.one)
            elif '/' in self.one:
                self.c1,self.c2=self.one.split('/')
                self.c1,self.c2=int(self.c1),int(self.c2)
                self.c=Fraction(self.c1,self.c2)
            self.one=input('请输入d的值:')
            if '/' not in self.one:
                self.d=float(self.one)
            elif '/' in self.one:
                self.d1,self.d2=self.one.split('/')
                self.d1,self.d2=int(self.d1),int(self.d2)
                self.d=Fraction(self.d1,self.d2)
            self.important=self.a*self.d
            self.b=self.important/self.c
            print('X等于(小数形式):',self.b)
            self.b=str(self.b)
            print('X(分数形式)等于:',Fraction(self.b))
        if super_big_ask=='c':
            self.one=input('请输入a的值:')
            if '/' not in self.one:
                self.a=float(self.one)
            elif '/' in self.one:
                self.a1,self.a2=self.one.split('/')
                self.a1,self.a2=int(self.a1),int(self.a2)
                self.a=Fraction(self.a1,self.a2)
            self.one=input('请输入b的值:')
            if '/' not in self.one:
                self.b=float(self.one)
            elif '/' in self.one:
                self.b1,self.b2=self.one.split('/')
                self.b1,self.b2=int(self.b1),int(self.b2)
                self.b=Fraction(self.b1,self.b2)
            self.one=input('请输入d的值:')
            if '/' not in self.one:
                self.d=float(self.one)
            elif '/' in self.one:
                self.d1,self.d2=self.one.split('/')
                self.d1,self.d2=int(self.d1),int(self.d2)
                self.d=Fraction(self.d1,self.d2)
            self.important=self.a*self.d
            self.c=self.important/self.b
            print('X等于(小数形式):',self.c)
            self.c=str(self.c)
            print('X等于(分数形式):',Fraction(self.c))
        if super_big_ask=='d':
            self.one=input('请输入a的值:')
            if '/' not in self.one:
                self.a=float(self.one)
            elif '/' in self.one:
                self.a1,self.a2=self.one.split('/')
                self.a1,self.a2=int(self.a1),int(self.a2)
                self.a=Fraction(self.a1,self.a2)
            self.one=input('请输入b的值:')
            if '/' not in self.one:
                self.b=float(self.one)
            elif '/' in self.one:
                self.b1,self.b2=self.one.split('/')
                self.b1,self.b2=int(self.b1),int(self.b2)
                self.b=Fraction(self.b1,self.b2)
            self.one=input('请输入c的值:')
            if '/' not in self.one:
                self.c=float(self.one)
            elif '/' in self.one:
                self.c1,self.c2=self.one.split('/')
                self.c1,self.c2=int(self.c1),int(self.c2)
                self.c=Fraction(self.c1,self.c2)
            self.important=self.b*self.c
            self.d=self.important/self.a
            print('X等于(小数形式):',self.d)
            self.d=str(self.d)
            print('X等于(分数形式):',Fraction(self.d))
        self.time.sleep(10)
ask=input('请输入需要计算分数吗：')
if ask =='否' or ask=='不用' or ask=='不需要':
    test=axe()
    test.Hello()
if ask=='需要' or ask=='是' or ask=='1':
    test=axe()
    test.fenshu()

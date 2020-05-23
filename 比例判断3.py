class bilibili:
    import time
    one,two=input('请输入一个比例:').split('=')
    one_one,one_two=one.split(':')
    two_one,two_two=two.split(':')
    one_one=float(one_one)
    one_two=float(one_two)
    two_one=float(two_one)
    two_two=float(two_two)
    def make(self):
        if self.one_one*self.two_two==self.one_two*self.two_one:
            print(self.one_one,'x',self.two_two,'=',self.one_one*self.two_two)
            print(self.one_two,'x',self.two_one,'=',self.one_two*self.two_one)
            print(self.one_one*self.two_two,'=',self.one_two*self.two_one)
            print(self.one_one,':',self.one_two,'=',self.two_one,':',self.two_two)
            print('所以这是个比例!')
        elif self.one_one/self.one_two==self.two_one/self.two_two:
            print(self.one_one,'÷',self.one_two,'=',self.one_one/self.one_two)
            print(self.two_one,'÷',self.two_one,'=',self.two_one/self.two_two)
            print(self.one_one,':',self.one_two,'=',self.two_one,':',self.two_two)
            print('这是一个比例!')
        else:
            print(self.one_one,'x',self.two_two,'=',self.one_one*self.two_two)
            print(self.one_two,'x',self.two_one,'=',self.one_two*self.two_one)
            print(self.one_one*self.two_two,'≠',self.one_two*self.two_one)
            print(self.one_one,':',self.one_two,'≠',self.two_one,':',self.two_two)
            print('所以这不是一个比例!')
        self.time.sleep(10)
test=bilibili()
test.make()
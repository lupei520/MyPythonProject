class bilibili:
    import time
    one_one=float(input("请输入第一个比的前项:"))
    one_two=float(input('请输入第一个比的后项:'))
    two_one=float(input('请输入第二个比的前项:'))
    two_two=float(input('请输入第二个比的后项:'))
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
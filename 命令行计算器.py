from fractions import Fraction
import decimal
import time
def Hello():
    print('加号为+,减号为-,乘号为*,除号为/(如果需要计算分数请将除号改为÷)')
    one=input('请输入一条算式:')
    if '*' in one:
        if '/' in one:
            if one.count('/')>=1:
                a1,a2=one.split('*')
                if '/' in a1 and '/' not in a2:
                    a,b=a1.split('/')
                    a,b,a2=int(a),int(b),float(a2)
                    A=Fraction(a,b)
                    B=a2
                    print(A,'*',B,'=',A*B)
                    time.sleep(10)
                elif '/' in a2 and '/' not in a1:
                    a,b=a2.split('/')
                    a,b,a1=int(a),int(b),float(a1)
                    A=Fraction(a,b)
                    B=a1
                    print(B,'*',A,'=',B*A)
                    time.sleep(10)
                elif '/' in a1 and '/' in a2:
                    a,b=a1.split('/')
                    c,d=a2.split('/')
                    a,b,c,d=int(a),int(b),int(c),int(d)
                    A=Fraction(a,b)
                    B=Fraction(c,d)
                    print(A,'*',B,'=',A*B)
        elif '%' in one:
            one=one.strip('%')
            a,b=one.split('*')
            a,b=decimal.Decimal(a),decimal.Decimal(b)
            print(a,'*',str(b)+'%','=',a*b/100)
            time.sleep(10)
        else:
            a,b=one.split('*')
            a,b=decimal.Decimal(a),decimal.Decimal(b)
            print(a,'*',b,'=',a*b)
            time.sleep(10)
    elif '/' in one and '+' not in one and '-' not in one:
        if '÷' in one:
            a1,a2=one.split('÷')
            if '/' in a1 and '/' not in a2:
                a,b=a1.split('/')
                a,b,a2=int(a),int(b),float(a2)
                A=Fraction(a,b)
                B=a2
                print(A,'/',B,'=',A/B)
                time.sleep(10)
            elif '/' in a2 and '/' not in a1:
                a,b=a2.split('/')
                a,b,a1=int(a),int(b),float(a1)
                A=Fraction(a,b)
                B=a1
                print(B,'/',A,'=',B/A)
                time.sleep(10)
            elif '/' in a1 and '/' in a2:
                a,b=a1.split('/')
                c,d=a2.split('/')
                a,b,c,d=int(a),int(b),int(c),int(d)
                A=Fraction(a,b)
                B=Fraction(c,d)
                print(A,'/',B,'=',A/B)
        elif '%' in one:
            one=one.strip('%')
            a,b=one.split('/')
            a,b=decimal.Decimal(a),decimal.Decimal(b)
            print(a,'/',str(b)+'%','=',a/b*100)
            time.sleep(10)
        else:
            a,b=one.split('/')
            a,b=decimal.Decimal(a),decimal.Decimal(b)
            print(a,'/',b,'=',a/b)
            time.sleep(10)
    elif '+' in one:
        if '/' in one:
            if one.count('/')>=1:
                a1,a2=one.split('+')
                if '/' in a1 and '/' not in a2:
                    a,b=a1.split('/')
                    a,b,a2=int(a),int(b),float(a2)
                    A=Fraction(a,b)
                    B=a2
                    print(A,'+',B,'=',A+B)
                    time.sleep(10)
                elif '/' in a2 and '/' not in a1:
                    a,b=a2.split('/')
                    a,b,a1=int(a),int(b),float(a1)
                    A=Fraction(a,b)
                    B=a1
                    print(B,'+',A,'=',B+A)
                    time.sleep(10)
                elif '/' in a2 and '/' in a1:
                    a,b=a1.split('/')
                    c,d=a2.split('/')
                    a,b,c,d=int(a),int(b),int(c),int(d)
                    A=Fraction(a,b)
                    B=Fraction(c,d)
                    print(A,'+',B,'=',A+B)
                    time.sleep(10)
        elif '%' in one:
            one=one.strip('%')
            a,b=one.split('+')
            a,b=decimal.Decimal(a),decimal.Decimal(b)
            print(a,'+',str(b)+'%','=',a+a*b/100)
            time.sleep(10)
        else:
            a,b=one.split('+')
            a,b=decimal.Decimal(a),decimal.Decimal(b)
            print(a,'+',b,'=',a+b)
            time.sleep(10)
    elif '-' in one:
        if '/' in one:
            if one.count('/')>=1:
                a1,a2=one.split('-')
                if '/' in a1 and '/' not in a2:
                    a,b=a1.split('/')
                    a,b,a2=int(a),int(b),float(a2)
                    A=Fraction(a,b)
                    B=a2
                    print(A,'-',B,'=',A-B)
                    time.sleep(10)
                elif '/' in a2 and '/' not in a1:
                    a,b=a2.split('/')
                    a,b,a1=int(a),int(b),float(a1)
                    A=Fraction(a,b)
                    B=a1
                    print(B,'-',A,'=',B-A)
                    time.sleep(10)
                elif '/' in a1 and '/' in a2:
                    a,b=a1.split('/')
                    c,d=a2.split('/')
                    a,b,c,d=int(a),int(b),int(c),int(d)
                    A=Fraction(a,b)
                    B=Fraction(c,d)
                    print(A,'-',B,'=',A-B)
                    time.sleep(10)
        elif '%' in one:
            one=one.strip('%')
            a,b=one.split('-')
            a,b=decimal.Decimal(a),decimal.Decimal(b)
            print(a,'-',str(b)+'%','=',a-a*b/100)
            time.sleep(10)
        else:
            a,b=one.split('-')
            a,b=decimal.Decimal(a),decimal.Decimal(b)
            print(a,'-',b,'=',a-b)
            time.sleep(10)
if __name__=='__main__':
    Hello()

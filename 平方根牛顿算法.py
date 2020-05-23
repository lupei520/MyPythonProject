def square_root_3():
    c=2
    g=c/2
    i=0
    while abs(g*g-c)>0.00000000001:
        g=(g+c/g)/2
        i+=1
    print('%.13f' %g)
square_root_3()
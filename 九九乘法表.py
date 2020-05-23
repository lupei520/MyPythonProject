def 九九乘法表():
    i=1
    while i<=9:     #外层循环，循环打印横!
        j=1
        while j<=i:       #内层循环，循环打印列!
            print(j,"x",i,"=",j*i,end=" ")     
            j+=1
        print()
        i+=1
九九乘法表()

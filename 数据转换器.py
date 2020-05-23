import os
import pickle
try:
    询问=input('请问你的文件的编码是UTF-8还是GBK(通常都是UTF-8,如果出错请输入GBK):')
    file_name=input('请输入文件名或者绝对路径:')
    file_data_name=input("请输入转化后的数据包的文件名:")
    if 询问=='UTF-8' or 询问=='utf-8':
        f1_UTF8版=open(file_name,'r',encoding='UTF-8')
        内容=f1_UTF8版.read()
        f2=open(file_data_name,'wb')
        pickle.dump(内容,f2)
        f2.close()
        print('文件成功转换成了名为%s的二进制文件' %file_data_name)
    if 询问=='GBK' or 询问=='gbk':
        f1_GBK版=open(file_name,'r',encoding='gbk')
        内容=f1_GBK版.read()
        f2=open(file_data_name,'wb')
        pickle.dump(内容,f2)
        f2.close()
        print('文件成功转换成了名为%s的二进制文件' %file_data_name)
except UnicodeDecodeError as r:
    print('你选择的编码出错了!,请重新输入编码!')
    print('系统错误原因:'+str(r))
except OSError as r:
    print('你要打包成二进制文件的那个文件的路径出错,或者这个文件根本不存在!')
    print('系统版错误原因:'+str(r))
finally:
    os.system('pause')
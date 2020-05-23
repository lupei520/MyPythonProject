import pickle
import os
def 解包():
    路径=input("请输入数据包的路径或者文件名:")
    f=open(路径,'rb')
    文本=pickle.load(f)
    file_name=input('请输入txt文件的名字(文件名+后缀):')
    储存=open(file_name,'w',encoding='UTF-8')
    储存.write(文本)
    储存.close()
    print("成功储存!")
    os.system('pause')
if __name__=='__main__':
    解包()
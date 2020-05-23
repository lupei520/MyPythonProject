import time
import os
def  txt_data():
    import pickle
    try:
        BM=input('请输入文件的编码(UTF8还是gbk):')
        file_name=input('请输入文件的名称或者路径:')
        file_data_name=input('请输入数据包的名称:')
        f=open(file_name,'r',encoding=BM)
        a=f.read()
        f1=open(file_data_name,'wb')
        pickle.dump(a,f1)
        f.close()
        f1.close()
        print('成功储存!')
    except OSError as r:
        print('请输入一个正确的路径!，该文件并不存在!')
        print('错误原因:'+str(r))
    finally:
        time.sleep(5)
        os.system('pause')
        f.close()

def data_txt():
    try:
        import pickle
        file_name=input('请输入data文件的路径:')
        file_txt_name=input('请输入txt文件的名字(要带后缀):')
        file_name_data=open(file_name,'rb')
        values=pickle.load(file_name_data)
        f=open(file_txt_name,'w',encoding='UTF-8')
        f.write(values)
        f.close()
        print('成功储存!')
    except  OSError as r:
        print('请输入一个正确的data文件的路径:')
        print('错误原因:'+str(r))
    except TypeError as r:
        print('------您的data文件是一个字典或者不是字符串类型,请使用无文件版进行转化!!!!!!------')
    finally:
        time.sleep(5)
        os.system('pause')
        f.close()
def data_print():
    try:
        import pickle
        file_name=input('请输入data文件的路径:')
        file_data=open(file_name,'rb')
        txt_print=pickle.load(file_data)
        print(txt_print)
    except OSError as r:
         print('请输入一个正确的data文件的路径:')
         print('错误原因:'+str(r))
    finally:
        time.sleep(5)
        os.system('pause')
        file_data.close()
ask=input('请问你要data转txt[有文件版](1)，还是txt转data(2),还是data转txt[无文件版](3)')
if ask=='1' or  ask=='data转txt[有文件版]':
    data_txt()
if ask=='2' or ask=='txt转data':
    txt_data()
if ask=='3' or ask=='data转txt[无文件版]':
    data_print()
    
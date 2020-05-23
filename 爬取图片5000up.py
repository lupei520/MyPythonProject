import requests
from lxml import etree
from bs4 import BeautifulSoup
import re
from threading import Thread
def One_5000():
    count=2485
    while True:
        url='https://seopic.699pic.com/photo/50151/'+str(count)+'.jpg_wh1200.jpg'
        res_head=requests.head(url)
        head=res_head.status_code
        if head==404:
            pass
        else:
            with open('图片地址5000.txt','a',encoding='utf-8') as f:
                f.write(url)
                f.write('\n')
        if count==2485+5000:
            break
        count+=1
def Two_5000():
    count=246
    while True:
        url='https://seopic.699pic.com/photo/40174/'+'0'+str(count)+'.jpg_wh1200.jpg'
        res_head=requests.head(url)
        head=res_head.status_code
        if head==404:
            pass
        else:
            with open('图片地址10000.txt','a',encoding='utf-8') as f:
                f.write(url)
                f.write('\n')
        if count==1000:
            break
        count+=1
def Download():
    path=input('请输入文件名或者路径:')
    f=open(path,'r',encoding='utf-8')
    count=1
    for i in f:
        url=i
        url=url.replace('\n','')
        url=url.replace(' ','')
        res=requests.get(url)
        with open(str(count)+'.jpg','wb') as f:
            f.write(res.content)
        count+=1
if __name__ == "__main__":
    T1=Thread(target=One_5000)   
    T2=Thread(target=Two_5000)
    T1.start()
    T2.start() 
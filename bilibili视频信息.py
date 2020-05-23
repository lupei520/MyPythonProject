import requests
import re
from bs4 import BeautifulSoup
from threading import Thread
def one_1000000():
    b=800000
    while True:
        url='https://www.bilibili.com/video/av'+str(b)
        res=requests.get(url)
        res.encoding='utf-8'
        soup=BeautifulSoup(res.text,'html.parser')
        for video in soup.select('.video-info'):
            title=video.find('h1')
            print('av'+str(b)+":"+video.text)
            if video.text==None:
                pass
            else:
                with open('This_is_one.txt',mode='a',encoding='utf-8') as f:
                    f.write('AV'+str(b)+':'+video.text)
                    f.write('\n')
                    f.write(url)
                    f.write('\n')
        b+=1
        if b==1000000:
            break
def two_2000000():
    b=1000001
    while True:
        url='https://www.bilibili.com/video/av'+str(b)
        res=requests.get(url)
        res.encoding='utf-8'
        soup=BeautifulSoup(res.text,'html.parser')
        for video in soup.select('.video-info'):
            title=video.find('h1')
            print('av'+str(b)+":"+video.text)
            if video.text==None:
                pass
            else:
                with open('This_is_two.txt','a',encoding='utf-8') as f:
                    f.write('AV'+str(b)+":"+video.text)
                    f.write('\n')
                    f.write(url)
                    f.write('\n')
        b+=1
        if b==2000000:
            break
def main():
    t1=Thread(target=one_1000000)
    t2=Thread(target=two_2000000)
    t1.start()
    t2.start()
if __name__ == "__main__":
    main()
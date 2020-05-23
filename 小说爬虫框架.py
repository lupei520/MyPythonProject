import requests
from bs4 import BeautifulSoup
import os
from threading import Thread
import sys
def one_200():
    a=28814679
    b=1
    while True:
        url='https://www.qqxs.cc/xs/91/91952/'+str(a)+'.html'
        res=requests.get(url)
        res.encoding='gbk'
        soup=BeautifulSoup(res.text,'html.parser')
        a+=1
        for news in soup.select('.zhangjieming'):
            news1=news.select('h1')[0].text
        with open('神医凰后章节目录前二百.txt','a',encoding='utf-8') as f:
            f.write(news1)
            f.write('\n')
            f.write(url)
            f.write('\n')
        b+=1
        if b==200:
            break
def two_400():
    a=28814892
    b=201
    while True:
        url='https://www.qqxs.cc/xs/91/91952/'+str(a)+'.html'
        res=requests.get(url)
        res.encoding='gbk'
        soup=BeautifulSoup(res.text,'html.parser')
        a+=1
        for news in soup.select('.zhangjieming'):
            news1=news.select('h1')[0].text
        with open('神医凰后章节目录前四百.txt','a',encoding='utf-8') as f:
            f.write(news1)
            f.write('\n')
            f.write(url)
            f.write('\n')
        b+=1
        if b==400:
            break
if __name__=='__main__':
    t=Thread(target=one_200)
    t1=Thread(target=two_400)
    t.start()
    t1.start()
            
import requests
import re
from bs4 import BeautifulSoup
url='https://www.bilibili.com/'
res=requests.get(url)
res.encoding='utf-8'
soup=BeautifulSoup(res.text,'html.parser')
big_div=soup.find('div',{'class','recommend-box'})
"""
for x in soup.find('div',{'class','recommend-box'}):
    count=re.search(r'((((\d+)\.)\d+)万播放)',x.text)
    if count==None:
        pass
    else:
        print(count.group())
"""
for y in big_div.find_all('div',{'class','info'}):
    title=y.find('p',{'class','title'})
    count=y.find('p',{'class','play'})
    print(title.text,end="  ")
    print(count.text)


        
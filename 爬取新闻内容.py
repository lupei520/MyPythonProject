import requests
from bs4 import BeautifulSoup
url=input('请输入网页地址:')
res=requests.get(url)
res.encoding='utf-8'
soup=BeautifulSoup(res.text,'html.parser')
for news in soup.select('.date-source'):
    news1=news.select('.date')[0].text
    news2=news.select('a')[0]["href"]
    news3=news.select('a')[0].text
    print(news1,news2,news3)
for news in soup.select('#article'):
    print(news.text)
with open('今日最新新闻内文数据.txt','w',encoding='utf-8') as f:
    f.write(news1)
    f.write(news2)
    f.write(news3)
    f.write(news.text)
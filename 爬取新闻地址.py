import requests
from bs4 import BeautifulSoup
k=[]
url='https://news.sina.com.cn/china/'
res=requests.get(url)
res.encoding='utf-8'
soup=BeautifulSoup(res.text,'html.parser')
for news in soup.select('.right-content'):
    news1=news.select('.news-1')[0].text
    news2=news.select('.news-2')[0].text
    print(news1,news2)
try:
    for x in soup.find_all('a'):
        print(x.text)
        print(x['href'])
        k.append(x.text)
        k.append('\n')
        k.append(x['href'])
        k.append('\n')
except KeyError:
    with open('Path新闻网址.txt','w',encoding='utf-8') as f:
        f.writelines(k)
        
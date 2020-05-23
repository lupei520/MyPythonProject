import requests
from bs4 import BeautifulSoup
a=4100
b=1
try:
    while True:
        url='http://seopic.699pic.com/photo/50053/'+str(a)+'.jpg_wh1200.jpg'
        res=requests.get(url)
        try:
            with open(str(a)+'jpg_wh1200.jpg','wb') as f:
                f.write(res.content)
                a+=1
                print('第'+str(b)+'张图片下载成功!')
        except:
            print('第'+str(b)+'张图片下载失败!')
        b+=1
except KeyboardInterrupt:
    print('欢迎再次使用!')
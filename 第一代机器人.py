
import json
import requests
import sys

def send_msg(url):
    headers = {'Content-Type': 'application/json;charset=utf-8'}
    data = {
        "msgtype": "link",
        "link": {
            "text": "博士狗:今天到谁学习了快点快点，别浪费时间,浪费时间的人可耻，知道吗?",
            "title": "Python学习",
            "picUrl": "图片连接",
            "messageUrl": "'https://oapi.dingtalk.com/robot/send?access_token=85d6bc0dbcb5f2ac32e7ca6222faf315469f47865eaa36ba0e995232d1f4d24d"
        }
    }
    r = requests.post(url,data = json.dumps(data),headers=headers)
    return r.text
if __name__ == '__main__':
   url = 'https://oapi.dingtalk.com/robot/send?access_token=48c1f4c38c2c533345f239aaa7e24541797932dcc998529f6c2fe094857bae51'                #此处为丁丁机器人的地址，参考技术手册创建
   print(send_msg(url))

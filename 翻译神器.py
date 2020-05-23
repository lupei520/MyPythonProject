import urllib.request
import urllib.parse
import json
while True:
 content=input('请输入需要翻译的内容:')
 url='https://fanyi.so.com/?src=onebox'
 head={}
 head['User-Agent']='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
 data={}
 data['i'] =content
 data['from']='AUTO'
 data['to']='AUTO'
 data['smartresult']='dict'
 data['client']= 'fanyideskweb'
 data['salt']='15834966698528'
 data['sign']= '83945adf071df74c22607b1f62510184'
 data['ts']='1583496669852'
 data['bv']='cc652a2ad669c22da983a705e3bca726'
 data['doctype']='json'
 data['version']='2.1'
 data['keyfrom']='fanyi.web'
 data['action']='FY_BY_REALTlME'
 data=urllib.parse.urlencode(data).encode('utf-8')
 rpg=urllib.request.urlopen(url,data)
 html =rpg.read().decode('utf-8')
 target=json.loads(html)
 print("翻译结果:%s" %(target["translateResult"][0][0]['tgt']))

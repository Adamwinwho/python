#网络爬虫
#1图片下载
#import urllib.request

#response = urllib.request.urlopen('http://placekitten.com/g/500/600')
#cat_img = response.read()

#with open('E:\\cat_500_600.jpg','wb') as f:
#    f.write(cat_img)

#2有道翻译
import urllib.request
import urllib.parse
import json

content = input('请输入要翻译的内容:')
url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=http://www.youdao.com/'

'''
head = {}
head['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36'
'''

data = {}
data['type'] = 'AUTO'
data['i'] = content
data['doctype'] = 'json'
data['xmlVersion'] = '1.8'
data['keyfrom'] = 'fanyi.web'
data['ue'] = 'UTF-8'
data['action'] = 'FY_BY_CLICKBUTTON'
data['typoResult'] = 'true'

data = urllib.parse.urlencode(data).encode('utf-8')
response = urllib.request.urlopen(url,data,head)

html = response.read().decode('utf-8')

target = json.loads(html)

print('翻译结果:%s' % (target['translateResult'][0][0]['tgt']))

import urllib.request
import urllib.parse
import json
import time

while True:
    content = input('请输入需要翻译的内容(输入"q!"退出程序):')
    if content == 'q!':
        break
    url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null"
    header = {}
    header['User-Agent']='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.0.10338 Safari/537.36'

    data = {}
    data['type'] = 'AUTO'
    data['i']= content
    data['doctype']='json'
    data['xmlVersion'] = '1.8'
    data['keyfrom'] = 'fanyi.web'
    data['ue'] = 'UTF-8'
    data['typoResult']='true'
    data = urllib.parse.urlencode(data).encode('utf-8')

    req = urllib.request.Request(url,data,header)
    response = urllib.request.urlopen(req)

    html = response.read().decode('utf-8')

    target = json.loads(html)

    print('翻译结果：%s' % (target['translateResult'][0][0]['tgt']))
    time.sleep(1)


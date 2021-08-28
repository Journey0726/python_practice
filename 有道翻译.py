import urllib.request
import urllib.parse
import json
import time
while True:
    content=input("请输入需要翻译的内容：（输入q！结束）")
    if content =='q!':
        break  
    url='http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
    data={}
    data['i']=content 
    data['from']= 'AUTO'
    data['to']= 'AUTO'
    data['smartresult']= 'dict'
    data['client']= 'fanyideskweb'
    data['salt']= '15955605900839'
    data['sign']= '79f3e2c5235e942493caa3d1b41bd9ad'
    data['ts']='1595560590083'
    data['bv']= '6275445dcf58d2f326d4a0dd44c9b352'
    data['doctype']= 'json'
    data['version']= '2.1'
    data['keyfrom']=' fanyi.web'
    data['action']= 'FY_BY_CLICKBUTTION'
    data=urllib.parse.urlencode(data).encode('utf-8')

    response = urllib.request.urlopen(url,data)
    html= response.read().decode('utf-8')

    target = json.loads(html)
    print('翻译结果：%s' % (target['translateResult'][0][0]['tgt']))
    time.sleep(3)

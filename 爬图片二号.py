import requests
import os
from lxml import etree
url= 'http://pic.netbian.com/4kmeinv/'
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3314.0 Safari/537.36 SE 2.X MetaSr 1.0'}
response = requests.get(url,headers = headers).text
tree = etree.HTML(response)
li_list=tree.xpath('//div[@class="slist"]//li')

if not os.path.exists('./pic'):
    os.mkdir('./pic')


for li in li_list:
    a=li.xpath('./a/img/@src')[0]
    a='http://pic.netbian.com'+a
    b=li.xpath('./a/img/@alt')[0]+'.jpg'
    b=b.encode('iso-8859-1').decode('gbk')
    pic = requests.get(url=a,headers=headers).content
    name = 'pic/'+b
    with open(name,'wb')as fp:
        fp.write(pic)
        print('success')

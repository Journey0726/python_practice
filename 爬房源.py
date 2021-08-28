import requests
from lxml import etree
url='https://changde.58.com/ershoufang/'
headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3314.0 Safari/537.36 SE 2.X MetaSr 1.0'}
response = requests.get(url,headers=headers).text
tree = etree.HTML(response)
a=tree.xpath('//ul[@class="house-list-wrap"]/li')
for li in a:
    title=li.xpath('./div[2]//a/text()')[0]
    print(title)
    

import requests
from lxml import etree
import re
import bs4
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3314.0 Safari/537.36 SE 2.X MetaSr 1.0'}
url = 'http://yuedu.sogou.com/book/info/EF1DF526CAC5BC2A9E75B29C30CFB5BF?w=1481&pos=1&'
response = requests.get(url= url,headers= headers).text
title = re.findall('<h1 class="detail-tit">(.*?)</h1>',response)[0]

url1= 'http://yuedu.sogou.com/book/view/EF1DF526CAC5BC2A9E75B29C30CFB5BF/653592412DA7DF0CC2846D1FAF50F676?w=1497&'
response1 = requests.get(url= url1,headers = headers).text
samlltitle = re.findall('<h2 class="book-title">(.*?)</h2>',response1)

tree = etree.HTML(response1)
#content1 = tree.xpath('//div[@id="book_653592412DA7DF0CC2846D1FAF50F676"]')
content1 = tree.xpath('//*[@id="book_653592412DA7DF0CC2846D1FAF50F676"]/div/div/p[1]//text()')
print(content1)
#for li in content1:
 #   content = li.xpath('.//p/text()')
  #  print(content)

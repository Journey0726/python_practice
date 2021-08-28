from selenium import webdriver
from lxml import etree
from selenium.webdriver.chrome.options import Options
bro=webdriver.Chrome(executable_path='D:\PYthon\chromedriver.exe')
bro.get('http://125.35.6.84:81/xk/itownet/portal/dzpz.jsp?id=3490572e2e9b409cb29db60518c8fa49')
page_text = bro.page_source
tree = etree.HTML(page_text)
li_list=tree.xpath("/html/body/div[4]/table/tbody")


for li in li_list:
    name = li.xpath('./tr/td[1]/text()')
    word=li.xpath('./tr/td[2]/text()')
    dict=(dict(zip(name,word)))
print(dict)
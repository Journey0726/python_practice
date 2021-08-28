from selenium import webdriver
import re

import time

bro=webdriver.Chrome(executable_path='D:\PYthon\chromedriver.exe')
bro.get('http://www.oh100.com/daxue/1970485.html')
response = bro.page_source
#response = response.encode('iso-8859-1').decode('utf-8')
list = re.findall('div class="content"(.*?)<script>',response,re.S)
list = str(list)
#list=list.replace('<p>','\n')
#list=list.replace('</p>','\n')
#list= list.replace('\u3000\u3000','  ')
#list = list.replace('</strong>',' ')
#list = list.replace('<strong>',' ')
with open('实践1.txt','w',encoding='utf-8') as file:
    file.write(list)
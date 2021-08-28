import bs4
import requests
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3314.0 Safari/537.36 SE 2.X MetaSr 1.0'}
url = 'https://www.17k.com/list/3183622.html'
response = requests.get(url=url,headers = headers).text
response = response.encode('iso-8859-1').decode('utf-8')

soup = bs4.BeautifulSoup(response,"html.parser")
big_title = soup.find("h1",class_='Title').text

detail = soup.select('.Volume > dd ')
with open (big_title+'.txt','w',encoding ='utf-8')as fp:
     for a in detail:
          detail_url=a.a['href']
          detail_url= 'https://www.17k.com/'+detail_url
          title = a.a.text
          detail_response=requests.get(url=detail_url,headers = headers).text
          detail_response =detail_response.encode('iso-8859-1').decode('utf-8')
          detail_soup = bs4.BeautifulSoup(detail_response,'lxml')
          content = detail_soup.find('div',class_="p").text
          fp.write(title+':'+content+'\n')
          print(title,'success')
     
     

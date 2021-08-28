import requests
import bs4

def open_url(url):
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3314.0 Safari/537.36 SE 2.X MetaSr 1.0'}
    res = requests.get(url,headers=headers)
    return res

def find_data(res):
    soup=bs4.BeautifulSoup(res.text,'html.parser')
    content = soup.find(id='Cnt-Main-Article-QQ')
    target=content.find_all("p",style="TEXT-INDENT: 2em")
    for each in target:
        print(each)



def main():
    url=('https://news.house.qq.com/a/20170702/003985.htm')
    res=open_url(url)
    find_data(res)
    
if __name__=='__main__':
    main()

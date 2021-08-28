import urllib.request

url='http://http://http://www.baidu.com'

proxy_support = urllib.request.ProxyHandler({'http':'102.129.249.120:3128'})

opener =urllib.request.build_opener(proxy_support)
opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3314.0 Safari/537.36 SE 2.X MetaSr 1.0')]

urllib.request.install_opener(opener)

response=urllib.request.urlopen(url)
html =response.read().decode('utf-8')
print(html)

import urllib.request

response = urllib.request.urlopen('http://b162.photo.store.qq.com/psb?/V12DhE9T37WouN/PVK49IRz.6nrsynCLviCeaXNzKHZi5mojDgw*hFtgIw!/b/dKIAAAAAAAAA&bo=KgIuAQAAAAAFByM!&rf=viewer_4')

picture=response.read()

with open('666.jpg',"wb") as f:
    f.write(picture)

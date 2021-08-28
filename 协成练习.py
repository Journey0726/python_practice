import asyncio

async def request(url):
    print('正在请求的url是',url)
    print('请求成功',url)
c= request('www.baidu.com')
loop=asyncio.get_event_loop()
loop.run_until_complete(c)
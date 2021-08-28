import time
import multiprocessing.dummy import Pool
def get_page(str):
    print('正在下载：',str)
    time.sleep(2)
    print('下载成功：',str)
start_time = time.time()
name_list=['1545','454','dfdf','dadf']
pool = Pool(4)
pool.map(get_page,name_list)
end_time = time.time()
print(end_time-start_time)

#coding=utf-8

import time
import requests
import re
import thread

url = 'http://www.heibanke.com/lesson/crawler_ex01/'
def spider(i):
    data = {'username': '123', 'password': i}
    r = requests.post( url=url, data=data )
    html = r.content
    response = html.find( '您输入的密码错误, 请重新输入' )
    print i, response,time.ctime().split(' ')[3]



for i in range(0,30):
    thread.start_new_thread(spider,(i,))
    time.sleep(1)
    
#利用多线程的方法来解决第二关：思路很简单，寻找html里是否有关键字 密码错误 没有密码错误关键词一看便知道

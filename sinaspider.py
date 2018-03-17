#本爬虫旨在扒取2018年科技栏目下头条
#coding=utf-8

import threading
import time
import requests
from bs4 import BeautifulSoup
import re
import sys



reload(sys)
sys.setdefaultencoding('utf-8')


def spidersina(month,day):
    url = 'http://tech.sina.com.cn/head/tech2018'           #0316am.'shtml'
    ram = requests.get(url + str(month)+str(day)+'am.shtml')
    htmlam = ram.content
    soupam = BeautifulSoup(htmlam)
    newsam = soupam.find_all(name='li',attrs={'data-sudaclick':re.compile('yaowenlist-\d')})
    rpm = requests.get( url + str( month ) + str( day )+'pm.shtml')
    htmlpm = rpm.content
    souppm = BeautifulSoup( htmlpm )
    newspm = souppm.find_all( name='li', attrs={'data-sudaclick': re.compile( 'yaowenlist-\d' )} )
    with open('E:\TestPy\lesson\sina.txt','a') as f:
        f.write('\n'+url + str(month)+str(day)+'am.shtml\n')
        f.write(month+'.'+day+'\n')
        for newam in newsam:
            if newam.string != None:
                f.write(newam.string)
        for newpm in newspm:
            if newpm.string != None:
                f.write(newpm.string)

def main():
    for month in range(1,4):
        for day in range (1,31):
            month = str(month).zfill(2)
            day = str(day).zfill(2)
            spidersina(month,day)


if __name__ == '__main__':
    main()

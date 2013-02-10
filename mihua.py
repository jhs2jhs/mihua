import urllib2
import time
from bs4 import BeautifulSoup
import webbrowser
import os
import subprocess as sp
import time
from datetime import datetime


def a():
    i = 0
    while i < 100:
        url = 'http://blog.sina.com.cn/s/blog_64b7517e0101g51h.html'
        url = 'http://blog.sina.com.cn/main_v5/ria/print.html?blog_id=blog_64b7517e0101g51h'
        url = 'http://hits.blog.sina.com.cn/hits?act=3&uid=64b7517e'
        url = 'http://hits.blog.sina.com.cn/hits?act=4&aid=64b7517e0101g51h&ref=http%3A%2F%2Fblog.sina.com.cn%2Fkeirawen&varname=requestId_89071200'
        req = urllib2.Request(url)
        response = urllib2.urlopen(req)
        page = response.read()
        print i, ' == ', len(page)
        soup = BeautifulSoup(page)
        divs = soup.find_all(name='span', attrs={'id':'r_64b7517e0101g51h'})
        print divs
        i = i + 1
        time.sleep(10)

def b():
    i = 0
    while i < 10:
        url = 'http://blog.sina.com.cn/s/blog_64b7517e0101g51h.html'
        webbrowser.open_new_tab(url)
        time.sleep(10)
        i = i + 1
        os.system('taskkill /F /IM chrome.app')
        time.sleep(10)
        
# http://www.daniweb.com/software-development/python/threads/213615/how-to-close-web-browser 
def c():
    url = 'http://blog.sina.com.cn/s/blog_64b7517e0101g51h.html'
    os.system('open -a safari %s'%url)
    url = 'http://v.youku.com/v_show/id_XNTEyOTM3MTgw.html'
    os.system('open -a safari %s'%url)
    #child = sp.Popen('chrome %s'%url, shell=True)
    #child = sp.Popen('open -a safari %s'%url, shell=True)
    time.sleep(20)
    #child.terminate()
    cmd = '''osascript -e 'tell application "safari" to quit'
'''
    os.system(cmd)

def c_loop():
    i = 0
    while True:
        print i, ' == ', str(datetime.now())
        try:
            c()
        except Exception, e:
            print e
        time.sleep(5)
        i = i + 1

def windows_d():
    url = 'http://blog.sina.com.cn/s/blog_64b7517e0101g51h.html'
    webbrowser.open_new_tab(url)
    url = 'http://v.youku.com/v_show/id_XNTEyOTM3MTgw.html'
    webbrowser.open_new_tab(url)
    time.sleep(20)
    os.system('taskkill /F /IM chrome.exe')
def windows_d_loop():
    i = 0
    while True:
        print i, ' == ', str(datetime.now())
        try:
            windows_d()
        except Exception, e:
            print e
        time.sleep(5)
        i = i + 1

if __name__ == '__main__':
    c_loop()
    windows_d()

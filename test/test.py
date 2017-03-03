import requests
import string
import sys
import zlib
from requests.packages import chardet
from StringIO import StringIO
import gzip
from cookielib  import LWPCookieJar
import os
s = requests.Session()
s.cookies = LWPCookieJar("cookiejar")
def login():
    url='http://jiaowu.swjtu.edu.cn/servlet/GetRandomNumberToJPEG'
    hraders={'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36',
             'Accept-Language':'zh-CN,zh;q=0.8',
             'Accept':'image/webp,image/*,*/*;q=0.8'}
    response=s.get(url,headers=hraders,stream=True)
    with open('demo.jpg','wb') as fd:
        for chunk in response.iter_content(128):
            fd.write(chunk)
            
  
    url='http://jiaowu.swjtu.edu.cn/servlet/UserLoginSQLAction'
    hraders={'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36',
             'Content-Type':'application/x-www-form-urlencoded',
             'Accept-Language':'zh-CN,zh;q=0.8',
             'Referer':'http://jiaowu.swjtu.edu.cn/service/login.jsp'}
    content = raw_input("please input:")
    data={'url':'../usersys/index.jsp',
          'OperatingSystem':'',
          'Browser':'',
          'user_id':'2014112155',
          'password':'123654789',
          'ranstring':''.join(content),
          'user_type':'student',
          'btn1':''}
    response=s.post(url,headers=hraders,params=data)   
    print response.status_code
    print response.text  
    
    url='http://jiaowu.swjtu.edu.cn/usersys/index.jsp'
    hraders={'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36',
             'Content-Type':'application/x-www-form-urlencoded',
             'Accept-Language':'zh-CN,zh;q=0.8',
             'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}
    response=s.get(url,headers=hraders)

def login_select_coures():
    url='http://jiaowu.swjtu.edu.cn/student/coursesys/MyCourseLeader.jsp'
    hraders={'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36',
             'Content-Type':'application/x-www-form-urlencoded',
             'Accept-Language':'zh-CN,zh;q=0.8',
             'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
             'Referer':'http://jiaowu.swjtu.edu.cn/servlet/StudentCourseSysCheckAction'}
    response=s.get(url,headers=hraders)
    print response.text
    url='http://jiaowu.swjtu.edu.cn:80/servlet/StudentCourseSysCheckAction'
    hraders={'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36',
             'Content-Type':'application/x-www-form-urlencoded',
             'Accept-Language':'zh-CN,zh;q=0.8',
             'Accept':'*/*'
             }
    response=s.get(url,headers=hraders)
    print response.text
    url='http://jiaowu.swjtu.edu.cn:80/student/coursesys/MyCourseLeader.jsp'
    hraders={'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36',
             'Content-Type':'application/x-www-form-urlencoded',
             'Accept-Language':'zh-CN,zh;q=0.8',
             'Accept':'*/*'
             }
    response=s.get(url,headers=hraders)
    print response.text
    
    url='http://jiaowu.swjtu.edu.cn/student/coursesys/MyCourseOther.jsp'
    hraders={'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36',
             'Content-Type':'application/x-www-form-urlencoded',
             'Accept-Language':'zh-CN,zh;q=0.8',
             'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
             'Referer':'http://jiaowu.swjtu.edu.cn/student/coursesys/MyCourseLeader.jsp'}
    response=s.get(url,headers=hraders)
    print response.text
if __name__=='__main__':
    login()
    login_select_coures()
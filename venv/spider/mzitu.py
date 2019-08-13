import requests
from lxml import etree
import time
import uuid
import os

import threading
import _thread


headers = {
    # 'accept': 'application/json, text/javascript',
    # 'accept-encoding': 'gzip, deflate, br',
    # 'accept-language': 'zh-CN,zh;q=0.9',
    # 'content-type': 'application/x-www-form-urlencoded',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
    'Referer': 'http://i.meizitu.net'

}

def get_one_page(url):
    response=requests.get(url,headers=headers)
    if response.status_code==200:
        result=etree.HTML(response.text)
        title=result.xpath("//li/a[@target='_blank']/@href")
        return title
    else:
        return None


def get_allpage(url):
    response=requests.get(url,headers=headers)
    time.sleep(0.5)
    if response.status_code==200:
        result=etree.HTML(response.text)
        num=result.xpath("//div[@class='pagenavi']/a[last()-1]/span/text()")
        return num[0]
    else:
        return None

def get_img_urls(url):
        time.sleep(0.1)
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            result = etree.HTML(response.text)
            # title = result.xpath("//div[@class='main-image']/a/@href")
            title = result.xpath("//p/a/img/@src")
            return title[0]
        else:
            return None

def save_imgs(url):
    dir=os.getcwd()
    time.sleep(0.1)
    name=str(uuid.uuid1())
    file=open(dir+"\\pic\\"+name+".jpg",'ab+')
    response = requests.get(url, headers=headers)
    file.write(response.content)
    file.close()
    pass


def main(start,end):
    list = []

    for i in range(start,end):
         print("进行到页数==="+str(i))
         try:
             url='https://www.mzitu.com/xinggan/'
             if(i!=1):
                 url=url+"page/"+str(i)
             print(url)
             pageurl=get_one_page(url)
             time.sleep(0.1)
             print(pageurl)
             #得到具体每一页
             for url in pageurl:
                 num=get_allpage(url)
                 print("个人专辑=="+url)
                 print(num)
                 for j in range(1,int(str(num))):
               #  for j in range(1,3):
                     if(j!=1):
                         src=get_img_urls(url+"/"+str(j))
                     else:
                         src=get_img_urls(url)

                     save_imgs(src)
         except BaseException:
             continue



def test(start,end):
    print(start)
    print(end)

if __name__ == '__main__':
    # t1=threading.Thread(target=main,args=(3,10))
    t2=threading.Thread(target=main,args=(85,95))
    # t3=threading.Thread(target=main,args=(71,80))
    # t4=threading.Thread(target=main,args=(81,90))
    # t5=threading.Thread(target=main,args=(91,100))
    # t6=threading.Thread(target=main,args=(100,110))
    # t1.start()
    t2.start()
    # t3.start()
    # t4.start()
    # t5.start()
    # t6.start()
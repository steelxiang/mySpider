import requests
from lxml import etree
#from spider.entity import movie


headers = {
    # 'accept': 'application/json, text/javascript',
    # 'accept-encoding': 'gzip, deflate, br',
    # 'accept-language': 'zh-CN,zh;q=0.9',
    # 'content-type': 'application/x-www-form-urlencoded',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'

}

def get_one_page(url):
    response=requests.get(url,headers=headers)
    if response.status_code==200:
        result=etree.HTML(response.text)
        dds=result.xpath("//dl[@class='board-wrapper']/dd")
        for dd in dds:
            rank=dd.xpath("//i[contains(@class,'board-index')]/text()")
            name=dd.xpath("/dd/p[@class='name']/text()")
            actor=dd.xpath("//p[@class='star']/text()")
            date=dd.xpath("//p[@class='releasetime']/text()")
            score_int=dd.xpath("//i[@class='integer']/text()")
            score_fraction=dd.xpath("//i[@class='fraction']/text()")
            pic=dd.xpath("//img[@class='board-img']/@src")
            print(rank)
            print(name)
            print(actor)
            print(date)
            print(score_int)
            print(score_fraction)
            print(pic)
            print("===========================")


        # return title
    else:
        return None

def main():
    url='https://maoyan.com/board/4'
    html=get_one_page(url)
    print(html)
if __name__ == '__main__':
    main()


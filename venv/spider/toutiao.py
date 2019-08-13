import requests
from urllib.parse import urlencode
import time





def get_page(offset,timestamp):
    headers = {
        # 'accept': 'application/json, text/javascript',
        # 'accept-encoding': 'gzip, deflate, br',
        # 'accept-language': 'zh-CN,zh;q=0.9',
        # 'content-type': 'application/x-www-form-urlencoded',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'

    }
    params={
        "aid":"24",
        "app_name":"web_search",
        "offset":offset,
        "keyword":"街拍",
        "count":"20",
        "en_qc":"1",
        "cur_tab":"search_tab",
        "pd":"synthesis",
        "timestamp":timestamp
    }
    url='https://www.toutiao.com/api/search/content/?'+urlencode(params)
    print(url)
    response=requests.get(url,headers=headers)
    try:
        if response.status_code==200:
            print(response.json())

    except requests.ConnectionError:
        print("error")




def main():
    for x in range(1,10):
        stamp=round(time.time()*1000)
        get_page(x*20,stamp)






if __name__ == '__main__':
    main()


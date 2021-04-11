import requests as re
import json

if __name__ == "__main__" :
    #一样的套路，进行UA伪装
    headers = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
    }
    url = 'https://movie.douban.com/j/chart/top_list?'
    param = {
        'type' : '17',
        'interval_id': '100:90',
        'action' :'',
        'start' :'1',#从库中第几部电影去取
        'limit' :'50'#一次请求取出的个数
    }
    response = re.get(url=url,params=param,headers=headers)
    list_data = response.json()
    with open("./douban.json",'w',encoding='utf-8') as fp:
        json.dump(list_data,fp=fp,ensure_ascii=False)
    print('爬取成功！')
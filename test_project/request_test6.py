import requests as re
import json
if __name__ == '__main__' :
    #目标是爬取国家药监局的信息
    #检查信息，发现是动态请求页面，ajax请求
    #进行UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
    }
    # 详情页的企业的详情数据也是动态加载出来的
    # http://scxk.nmpa.gov.cn:81/xk/itownet/portal/dzpz.jsp?id=ed59438f34ae47e794f4c7ee5137c1f7
    # http://scxk.nmpa.gov.cn:81/xk/itownet/portal/dzpz.jsp?id=be76b514d896439dba33115f228a6ce9
    # 观察后发现，所有详情页的post请求的url只有id不一样，其余的都相同
    # 通过对详情页URL的观察，发现URL的域名都是一样的，只有携带的参数(id)不一样
    # 可以通过域名和id值拼接出一个完整的企业对应的详情页的URL
    #如果可以批量获取多家企业的id后，就可以将id和url形成一个完整的详情页对应详情数据的ajax请求的url
    url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'
    #参数的封装
    data = {
         'on': 'true',
         'page': '1',
         'pageSize': '15',
         'productName': '',
         'conditionType': '1',
         'applyname':'',
         'applysn':'',
                }

    json_ids = re.post(url=url,headers=headers,data=data).json()
    id_list = []#专门来存储企业id
    all_data_list = []#存储所有企业信息
    for dic in json_ids['list'] :#选择字典中的list列表，并遍历列表
        id_list.append(dic['ID'])#选择列表中的id值并添加到新列表中
    #获取企业详情信息
    get_url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'
    for id in id_list :#选择列表并遍历列表
        data = {
            'id' : id
         }#遍历时，传送不同的id值
        detail_json = re.post(url=get_url,headers=headers,data=data).json()#返回一个被解析为json格式的Promise 对象
        all_data_list.append(detail_json)#将json添加到新列表中去
    #持久化存储
    with open('./all_data.json','w',encoding='utf-8') as fp:
        json.dump(all_data_list,fp=fp,ensure_ascii=False)
        print('爬取成功！')

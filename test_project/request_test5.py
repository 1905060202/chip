import requests as re
#查询肯德基餐厅位置信息
#检查页面，可以发现response headers里面的content-type是text类型，而Request Method是Post故使用post()请求获取信息
if __name__ == '__main__' :
    #UA伪装技术
    headers = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
    }
    #开始第一步，指定url
    url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'#注意不要删除op=keyword
    #第二步，开始发送请求,首先要进行post请求参数处理
    post_op = input('请输入要查询的城市：')
    data = {
        'cname':'',
        'pid':'',
        'keyword': post_op,
        'pageIndex': '1',
        'pageSize': '79'
    }
    response = re.post(url=url,data=data,headers=headers)
    #第三步，获取响应数据
    kendeji = response.text
    #第四步，持久化存储
    filename = post_op + '.text'
    with open (filename,'w',encoding='utf-8') as fp :
        fp.write(kendeji)
    print("爬取成功！")
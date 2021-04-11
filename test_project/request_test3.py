import requests as re
import json
if __name__ == "__main__" :
    #因为存在UA检测反扒机制，故一定要用UA伪装
    headers = {
        'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
    }
    #指定url
    post_url = 'https://fanyi.baidu.com/sug'
    #post请求参数处理(同get请求一一致)
    word = input("输入单词：")
    data = {
        'kw' : word
    }
    #返回一个响应对象
    response = re.post(url=post_url,data=data,headers=headers)#实现请求的发送
    #获取响应数据。json()方法返回的是obj(如果确认服务器响应数据是json类型的才可以使用)
    mybaby = response.json()
    #持久化存储
    filename = word + '.json'#如果不执行这步操作，那么文件在d盘根目录生成
    fp = open(filename,'w',encoding='utf-8')
    json.dump(mybaby,fp=fp,ensure_ascii=False)#获取的信息是中文，故不能同ascii码
    fp.close()
    print('数据爬取结束')
    #如果json出了问题，记得检查一下url
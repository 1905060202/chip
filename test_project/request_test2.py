import requests as re
#UA伪装 : 让爬虫对应的请求载体身份伪装成浏览器
#UA : User-Agent(请求载体的身份标识),如果检测到请求的载体身份标识是浏览器，那么代表是正常请求
#但是如果请求的载体身份标识不是基于某一款浏览器的，则表示该请求为不正常的请求
#如果是不正常请求，那么服务器端可能会拒绝请求
if __name__ == "__main__":
    #UA伪装 : 将对应的User-Agent封装到一个字典中
    headers = {
        'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
    }
    url = 'https://www.baidu.com/s'
    #处理url携带的参数：封装到字典中
    kw = input("enter a word:")
    param = {
        'wd':kw
    }
    #对指定url发起的请求对应的url是携带参数的，并且请求过程中处理了参数
    response = re.get(url=url,params=param,headers=headers)#相当于做了拼接
    page_text = response.text
    filename = kw + ".html"
    with open(filename,'w',encoding = 'utf-8') as fp :
        fp.write(page_text)
    print(filename+"保存成功")
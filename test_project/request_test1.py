import requests as re
if __name__ == "__main__":
    #指定url
    url = "https://www.baidu.com/"
    #发起请求
    #get方法会返回一个响应对象
    response = re.get(url=url)
    #获取响应数据
    page_text = response.text#返回一组字符串形式的响应数据
    print(page_text)
    #持久化存储
    with open('./baidu.html','w',encoding='utf-8') as fp:
        fp.write(page_text)
    print("爬取数据结束")

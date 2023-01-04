# 由于是外网，需要使用代理，不使用工具类
# 本程序专为 从https://hanime1.me/comics 下载舰娘本子
import time
import requests
from  selenium import  webdriver
#encoding="utf-8"
import re
import os
from bs4 import BeautifulSoup
global TITLE_TEXT
TITLE_TEXT = 1

# 封装一个方法，输入网址和文件夹，会将该网址下所有图片下载到该文件夹
def one_page_download(page_url):
    global TITLE_TEXT
    proxie = {
        "http": "http://127.0.0.1:33210",
        "https": "http://127.0.0.1:33210",
    }

    # 此处使用selenium而不是requests来抓取数据，因为是动态加载的
    option = webdriver.ChromeOptions()
    option.add_argument(r'user-data-dir=C:\Users\li\AppData\Local\Google\Chrome\User Data')
    option.add_argument("blink-settings=imagesEnabled=false")
    # driver = webdriver.Chrome(options=option)
    driver = webdriver.Chrome()
    driver.get(page_url)

    #selenium加载较慢，等待10秒
    time.sleep(1)
    text = driver.page_source.lower()
    driver.close()

    # 正则每一个图片地址    https://t.nhentai.net/galleries/1613703/1t.jpg
    ree = r"https://t.nhentai.net/galleries/\d{6,8}/\d{1,2}t.jpg"
    s = re.findall(ree,text)
    print(s)


    imgEndUrl = []
    # 对字符串修正得到真正的地址 https://i.nhentai.net/galleries/1613703/1.jpg
    for i in s:
        x = list(i)
        x[8] = "i";
        x[len(x)-5] = "";
        imgEndUrl.append("".join(x))


    os.mkdir(str(TITLE_TEXT))  # 根据标题建立文件夹

    # 单张下载
    i = 1
    for url in imgEndUrl:
        time.sleep(1)
        r = requests.get(url,proxies=proxie)
        r.status_code

        with open(str(TITLE_TEXT)+"\\"+str(i)+".jpg","wb") as fp:
            fp.write(r.content)

        print("本页第"+str(i)+"张图片完成")
        print("当前时间： ", time.strftime('%Y.%m.%d %H:%M:%S ', time.localtime(time.time())))
        i += 1

    TITLE_TEXT += 1     # 文件夹名加1

# 根据两个页面来获取所有文章链接接
def by_home_sel_page():
    # 第一页
    url1 = r"https://hanime1.me/comics/search?query=Monaka+"
    # 第二页
    url2 = r"http://hanime1.me/comics/search?query=Monaka&page=2"
    driver = webdriver.Chrome()
    driver.get(url1)
    # selenium加载较慢，等待10秒
    time.sleep(1)
    text = driver.page_source.lower()

    # 第二页
    driver = webdriver.Chrome()
    driver.get(url2)
    # selenium加载较慢，等待1秒
    time.sleep(1)
    text += driver.page_source.lower()
    driver.close()

    # 正则 <a style="text-decoration: none;" href="https://hanime1.me/comic/45508">
    ree = r'''https://hanime1.me/comic/\d{2,8}'''
    pages = (re.findall(ree,text))     # 获得所有页面链接

    # 遍历，依次调用单篇完成所有的下载
    i = 0
    for page in pages:
        one_page_download(page)    # 单篇调用
        i += 1
        # 单篇下载完成后提示
        print("第"+str(i)+"篇文章下载完成"+"    "+"当前时间： ", time.strftime('%Y.%m.%d %H:%M:%S ', time.localtime(time.time())))
        time.sleep(5)
by_home_sel_page()

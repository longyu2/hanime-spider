import json
import math
import bs4
from selenium import webdriver
from bs4 import BeautifulSoup
from get_proxy import requests_proxy
import requests
import get_proxy
import headers
import requests
import file
# 本函数用来抓取某个页面，


def get_html(httpurl):
    r = requests.get(httpurl, proxies=get_proxy.requests_proxy, headers=headers.headers, cookies=headers.cookies)
    return r.text

# 本函数用来解析html，并生成json
def html_to_json(htmltext):
    # text=""
    # 这里是把一个html页面下载到了文件中提升查找速度
    # with open('1.html','r',encoding='utf8') as fp:
    #     text = fp.read()
    # 使用bs4获取每篇文章所在盒子
    soup = BeautifulSoup(htmltext, 'html.parser')
    divs = soup.select('.comic-rows-videos-div')

    # 从整个页面中主要提取出3个信息 1.文章url,方便根据文章访问  2.源图片url，只要数字编号  3。name 本子名
    # 定义一个列表来存储,列表的每一项包含这三个信息，这个列表代表一页的所有本子
    arrs_page = []

    # div 表示每篇文章的那个盒子，divs表示所有盒子的合集，从div中即可提取出每篇文章的三种信息
    for div in divs:
        # print(div.contents)
        content_img_url = div.find('img').get(
            'data-srcset')   # 获取每个本子封面的url，这个url中的数字就是存放源图片的地址
        img_url_number = ''.join(filter(str.isdigit, content_img_url))
        content_article_url = div.find('a').get('href')  # 文章网址
        content_article_name = div.find(
            'div', class_='comic-rows-videos-title').string

        arrs_page.append({'img_url_number': img_url_number, 'content_article_url': content_article_url,
                         'content_article_name': content_article_name})

    # 将一页的所有数据存入json文件,这代表搜索某个关键词后，整页的文章的信息，还需要根据页数才能拥有所有索引
    jsonstr = json.dumps(arrs_page, ensure_ascii=False)
    return jsonstr
   
# 前面只get到了一页的信息，这次获取一个关键词的所有页
# 思路是根据tag上的数量判断有几页,首先获取首页的html,再从首页中提取出带有数量的那个标签
def getALL():
    tag = input("请输入标签名：目前只支持根据标签下载，请输入准确的标签！")
    home_url = "https://hanime1.me/characters/" + \
        tag.replace(" ", '%20')     # 空格转化成url中%20
   
    home_html = get_html(home_url)
    # 使用bs4解析html提取出带有数量的那个标签
    soup = bs4.BeautifulSoup(home_html, 'html.parser')

    #  # 根据嵌套关系得到数量 
    tag_count = soup.find(attrs={'id': 'comics-search-tag-top-row'})
    tag_count = int(tag_count.h2.div.div.text)
  
   
    #  将tag名和count保存到字典
    tag_and_count = {'tag_name': tag, 'count': tag_count}
    print(tag_and_count)

    page_count = math.ceil(int(tag_and_count['count'])/30)  # 每页30，除去30得到页数

    print(type(page_count))
    # 得到页数后构建url数组，

    # 空列表存储所有json
    ALL_PAGE_JSON = []
    for i in range(1, page_count+1):
        page_url = home_url+'?page='+str(i)
        json_page = json.loads(html_to_json(get_html(page_url)))
       

        ALL_PAGE_JSON.extend(json_page)     # 每页所有json追加
        # print

        print('第'+str(i)+'页解析完成')

    # 把json中空格替换为下划线不然没办法存储为文件
    tag_and_count['tag_name'] = tag_and_count['tag_name'].replace(" ", "_")
    tag_and_count['tag_name'] = tag_and_count['tag_name'].replace("|", "_or_")

    with open('JSONS/tag['+tag_and_count['tag_name']+'].json', 'w', encoding='utf8') as fp:
        fp.write(json.dumps(ALL_PAGE_JSON, ensure_ascii=False))
    print("所有页的json已经追加完成，已存储到json文件中！")

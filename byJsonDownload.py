# 本文件是正式下载
import datetime
import json
import os
import time
import file
import requests
from get_proxy import requests_proxy
import urllib3
urllib3.disable_warnings()


# https://hanime1.me/comic/78548  这个是该本子的网址，78548是它的编号，它还有一个数字，也就是地址的编号，用来存储图片
# 如https://hanime1.me/comic/urlnumber/ 中的urlnumber 就是这个本子图片的存储地址的编号，也是唯一的，只要拿到它，就可以下载完一篇本子了
# 该网站存储图片的网址为  https://hanime1.me/comic/urlnumber/   urlnumber存储地址编号

# 2个参数，图片存储地址编号，目标文件夹
def download_img_by_number(number, folder):
    index = number
    max = 1000
    for i in range(1, max):
        while(True):
            try:
                start_time = time.time()
                req = requests.get('https://i.nhentai.net/galleries/' +
                                index+'/'+str(i)+'.jpg', proxies=requests_proxy, headers={'Connection':'close'},verify=False)
            except:
                print("请求时出现错误，已经成功抛出异常")
                print("3秒后自动重新发起请求")
                time.sleep(3)
                continue
            finally:
                break
        download_end_time = time.time()
        print(str(datetime.datetime.now())+"\t\t"+"该文章第"+str(i)+"张图片完成", end=" ")
        print("下载完成花费时间为:{}秒".format(download_end_time-start_time) ,end=" ")
        if req.status_code != 200:
            print(str(datetime.datetime.now())+"\t\t"+"该文章全部完成")
            break
        with open(folder+'/'+str(i)+'.jpg', 'wb') as fp:
            fp.write(req.content)
        
        end_time = time.time()

        print("存储于文件夹花费时间为:{}秒".format(end_time-start_time))
        

# 根据json里存储的信息，调用download函数进行批量下载
def byJsonDownload(Path_and_fileName, outputFolder):

    # Path_and_fileName 是一个字典，存储着json文件的路径和文件名
    jsonFileName = Path_and_fileName["filename"]            # 使用jsonFileName存储json文件名
    
    # PathAndName 存储json的完整路径
    PathAndName = os.path.join(
        Path_and_fileName["path"], Path_and_fileName["filename"])

   
    # 读取json文件，并转换为字典列表
    json_tag_dict = json.loads(file.read(PathAndName, 'r'))     

    if(os.path.exists(outputFolder+'/'+jsonFileName.replace(".json",""))):
        print("tag目录已经存在，本次不用创建")
    
    else:
         # 在指定的输出文件夹中，根据json文件名建立目录，并将json文件写入目录中
        os.mkdir(outputFolder+'/'+jsonFileName.replace(".json",""))
        file.write(outputFolder+'/'+jsonFileName.replace(".json","")+'/'+jsonFileName,'w',(file.read(PathAndName, 'r')))
       

    print("开始！本次下载的标签为："+jsonFileName+"，本次共有"+str(len(json_tag_dict))+"篇本子需要下载")
    num = 1
   
    # 读取之后，遍历每一篇本子，同时调用download函数下载
    for i in json_tag_dict:
        # if num <= 33:
        #     num+=1
        #     continue
        number = i['img_url_number']
        url = i['content_article_url']
        name = i['content_article_name']
        name = name.replace('/','_').replace('|',"").replace(',',"")

        # 根据本子名创建文件夹，并且在里面放一个包含该本子三个信息的txt
        os.mkdir(outputFolder+'/'+jsonFileName.replace(".json","")+'/'+str(num))

        with open(outputFolder+'/'+jsonFileName.replace(".json","")+'/'+str(num)+'/readme.txt','w',encoding='utf8') as fp:
            fp.write("该本子的网页地址为："+url+'\n'+'该本子图片存储地址编号为：'+number+'\n'+'该本子名为：'+name)

        download_img_by_number(number,outputFolder+'/'+jsonFileName.replace(".json","")+'/'+str(num))
        print(str(datetime.datetime.now())+"\t\t"+"第"+str(num)+"篇本子下载完成")
        num+=1

# byJsonDownload(input("请输入json路径"),input("请输入输出文件夹路径"))
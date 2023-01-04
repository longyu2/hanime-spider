import datetime
import json
import requests
import file
from  get_proxy import requests_proxy

def download_img_by_number(number,folder):
    # 代理，外网必须用
   
    index = number
    max = 1000
    for i in range(1,max):
        req = requests.get('https://i.nhentai.net/galleries/'+index+'/'+str(i)+'.jpg', proxies=requests_proxy)
        if req.status_code != 200:
            print(str(datetime.datetime.now())+"\t\t"+"该文章全部完成")
            break
        with open(folder+'/'+str(i)+'.jpg', 'wb') as fp:
            fp.write(req.content)
        print(str(datetime.datetime.now())+"\t\t"+"该文章第"+str(i)+"张图片完成")
 

download_img_by_number("2274491",r"S:\Desktop\test")
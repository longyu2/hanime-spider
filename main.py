# 程序入口，可选择所有功能

import os
import byJsonDownload
import getHtmlToJson
import file
import json


option_str = '\
1. 根据标签下载为json(仅输入一个标签，只下载为json)\n\
2. 根据json批量下载(仅根据已经存在的json下载)\n\
3. 单篇本子下载\n\
4. 根据标签下载为json并且下载为图片,为2和5的聚合版本，功能最直接，不会存储为json，而是直接下载为图片\n\
5. 批量根据标签下载为json，为选项1的扩展版本\n\
'

input_number = int(input("请输入需要的功能选项：\n"+option_str))
if(input_number == 1):
    tag = input("请输入tag名，注意，一定要正确输入：")
    output_folder = input("请输入output文件夹")
    getHtmlToJson.save_json(tag,output_folder)
   
elif(input_number == 2):
    jsons_path = '待下载队列'
    output_folder = input("请指定目标目录:")
    ALL_list = []
    print("待加载文件有：")
    # 获取待加载文件夹下所有文件
    for path, d, filelist in os.walk(jsons_path):
        for filename in filelist:
            item = (os.path.join(path, filename))
            ALL_list.append({"path":path,"filename":filename})
            print(item)

    # 主进程，循环读取文件，调用 byJsonDownload
    for i in ALL_list:
        print(i)
        byJsonDownload.byJsonDownload(i, output_folder)
elif(input_number == 3):
    # 单篇下载输入文章图片源编号即可
    num = input("输入文章图源编号")
    folder = input("输入文件夹路径")
    byJsonDownload.download_img_by_number(num,folder)
elif(input_number == 4):
    print("此功能正在开发，敬请期待")
elif(input_number == 5):
    a=""
    while(a!='y'):
        a = input("请更改文件夹中 待下载tag.json 文件,更改好后输入y确认进行下载")
    download_tags = json.loads(file.read('待下载tags.json','r'))
    output_folder = input("请输入output文件夹")
    # 循环下载为json
    for tag in download_tags:
        getHtmlToJson.save_json(tag,output_folder)
    
else:
    print("请正确输入！")


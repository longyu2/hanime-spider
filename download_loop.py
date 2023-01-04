# 本文件用来根据待下载队列中的所有json文件，批量下载
import os
import random
import byJsonDownload
import file

# PATH = print(os.getcwd())

# jsons_path = input("请输入所有json文件存储的目录：如默认值，请输入1:")
# if jsons_path == '1':
#     jsons_path == './待下载队列'
jsons_path = '待下载队列'


output_folder = input("请指定目标目录:")
# output_folder = "D:\hanime_out"

# for i in range(1,10):
#     file.write("./待下载队列/"+str(i)+'.txt','w',str(random.randint(0,100)))


ALL_list = []

print("待加载文件有：")
# 获取待加载文件夹下所有文件
for path, d, filelist in os.walk(jsons_path):
    for filename in filelist:
        item = (os.path.join(path, filename))
        ALL_list.append({"path":path,"filename":filename})
        print(item)


# 主进程，循环读取文件，调用main的 byJsonDownload

for i in ALL_list:
    print(i)
    byJsonDownload.byJsonDownload(i, output_folder)
    
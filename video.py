# 本模块用于下载视频资源
import requests
import requests
from tqdm import tqdm
import requests
from get_proxy import requests_proxy


def download(url: str, fname: str):
    # 用流stream的方式获取url的数据
    resp = requests.get(url, proxies=requests_proxy ,verify=False,stream=True)
    # 拿到文件的长度，并把total初始化为0
    total = int(resp.headers.get('content-length', 0))
    # 打开当前目录的fname文件(名字你来传入)
    # 初始化tqdm，传入总数，文件名等数据，接着就是写入，更新等操作了
    with open(fname, 'wb') as file, tqdm(
        desc=fname,
        total=total,
        unit='iB',
        unit_scale=True,
        unit_divisor=1024,
    ) as bar:
        for data in resp.iter_content(chunk_size=1024):
            size = file.write(data)
            bar.update(size)

if __name__ == "__main__":
    # 下载文件，并传入文件名
    url = "https://cdn5-videos.motherlessmedia.com/videos/A540708-720p.mp4"
    download(url, "video.mp4")





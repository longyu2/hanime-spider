import json
import file
import requests

cookies = {
    '_ga': 'GA1.2.1622132898.1653587732',
    '__gads': 'ID=bca818071e624083-22a3b0fe6ad3004a:T=1653651554:RT=1653651554:S=ALNI_MYnuVdTjx3XmDVLN3dQ7DL2LiUPDQ',
    'quality': '1080',
    '__atssc': 'google%3B1',
    'cf_clearance': 'aK4m9_6TyySNHczjpAb3BjRsCqaUnSf05qTO07PXh68-1672769632-0-150',
    '_gid': 'GA1.2.67930034.1672769636',
    '__gpi': 'UID=000005da14792e19:T=1653651554:RT=1672769636:S=ALNI_MaUL_HuDz5wUc84rfWUfq_jl-BCYQ',
    '__cf_bm': 'mBgS0K2cfK9p71QW__WvPJ7z7j0KvISE6P1B6uKNKS0-1672770539-0-AfvGFmrtkIDYqycKLeuBHuTobzyPOykk+fqJeZ/F9T47CnDkOSXNu12n8vgK8OUNZ0HwRKVIiNjK48tf3fPpu7uGajs4sLKqA2tUErANmR/MGy3TDeHKfBcJFaNHEBYskV0DMY2H/Fwjtv7zipVmRrA=',
    '__atuvc': '2%7C49%2C0%7C50%2C2%7C51%2C8%7C52%2C4%7C1',
    '__atuvs': '63b472e07ac31ed5003',
    'XSRF-TOKEN': 'eyJpdiI6ImJlTUtLN3ZQWTBEMzUxRjdHaXhsdEE9PSIsInZhbHVlIjoiY1VWYWxZclFiVmpmTlZ5WWlVOFdTdUxcLzdVRG5jN0JcL3JnbHZwN1orYno0VkxSUEV4NThyZWZ6MEY3bnFPZFQwIiwibWFjIjoiZmVhYTk0ZmNjMWMyNTkzYTE5YmI5YWQ1NzNlN2E0NzU1MWY1MzE4NzM1MDM5NmVkZmUzM2Y3MmQwNjcwNmNkZiJ9',
    'hanime1_session': 'eyJpdiI6ImNPZW1hdFV5ODF4RmxMYytBS2pUK1E9PSIsInZhbHVlIjoiZFNqM2FcL01BVzRHellYTkZkYUJUT3BSUGM3Qk9UTks5cElROW1sSjRVZllnamcySFJIZDBFK0U1blRSdHlGMlMiLCJtYWMiOiJhMDU2NDgxYmNhYmM1YjJkNmRkODI5ZGE1NDhlYzE1YzIwYWZmOTBkYjZiOTU3MDQ1YmE1YjgxZTM4MzJhNTU5In0%3D',
}

headers = {
    'authority': 'hanime1.me',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'max-age=0',
    # 'cookie': '_ga=GA1.2.1622132898.1653587732; __gads=ID=bca818071e624083-22a3b0fe6ad3004a:T=1653651554:RT=1653651554:S=ALNI_MYnuVdTjx3XmDVLN3dQ7DL2LiUPDQ; quality=1080; __atssc=google%3B1; cf_clearance=aK4m9_6TyySNHczjpAb3BjRsCqaUnSf05qTO07PXh68-1672769632-0-150; _gid=GA1.2.67930034.1672769636; __gpi=UID=000005da14792e19:T=1653651554:RT=1672769636:S=ALNI_MaUL_HuDz5wUc84rfWUfq_jl-BCYQ; __cf_bm=mBgS0K2cfK9p71QW__WvPJ7z7j0KvISE6P1B6uKNKS0-1672770539-0-AfvGFmrtkIDYqycKLeuBHuTobzyPOykk+fqJeZ/F9T47CnDkOSXNu12n8vgK8OUNZ0HwRKVIiNjK48tf3fPpu7uGajs4sLKqA2tUErANmR/MGy3TDeHKfBcJFaNHEBYskV0DMY2H/Fwjtv7zipVmRrA=; __atuvc=2%7C49%2C0%7C50%2C2%7C51%2C8%7C52%2C4%7C1; __atuvs=63b472e07ac31ed5003; XSRF-TOKEN=eyJpdiI6ImJlTUtLN3ZQWTBEMzUxRjdHaXhsdEE9PSIsInZhbHVlIjoiY1VWYWxZclFiVmpmTlZ5WWlVOFdTdUxcLzdVRG5jN0JcL3JnbHZwN1orYno0VkxSUEV4NThyZWZ6MEY3bnFPZFQwIiwibWFjIjoiZmVhYTk0ZmNjMWMyNTkzYTE5YmI5YWQ1NzNlN2E0NzU1MWY1MzE4NzM1MDM5NmVkZmUzM2Y3MmQwNjcwNmNkZiJ9; hanime1_session=eyJpdiI6ImNPZW1hdFV5ODF4RmxMYytBS2pUK1E9PSIsInZhbHVlIjoiZFNqM2FcL01BVzRHellYTkZkYUJUT3BSUGM3Qk9UTks5cElROW1sSjRVZllnamcySFJIZDBFK0U1blRSdHlGMlMiLCJtYWMiOiJhMDU2NDgxYmNhYmM1YjJkNmRkODI5ZGE1NDhlYzE1YzIwYWZmOTBkYjZiOTU3MDQ1YmE1YjgxZTM4MzJhNTU5In0%3D',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
}



proxies = json.loads(file.read("./proxie.json",'r'))

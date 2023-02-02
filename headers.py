import json
import file
import requests
from get_proxy import requests_proxy
import requests

import requests

cookies = {
    '__gads': 'ID=7f96118d9d1306a1-22d557512ed900bb:T=1673107879:RT=1673107879:S=ALNI_MbTqF10HkGZkXWkMmFxCE2tf6EErQ',
    '_ga': 'GA1.2.1731675392.1673107870',
    '__gpi': 'UID=00000b9f4fd7f0ca:T=1673107879:RT=1675168820:S=ALNI_MatOysPCRiuGJHlY9zCxCq7Y4uSBA',
    'cf_clearance': 'CZy2TgB6bNhmG7ohtSqR9ptLlH4y2QVpVISIDgWbxas-1675175850-0-150',
    '__atuvc': '9%7C5',
    'XSRF-TOKEN': 'eyJpdiI6ImRZRkVcL2JWWVwvOHBqQjNzeGEweFJjdz09IiwidmFsdWUiOiJBZHQ3TXN1TmtcL21JRjdMM1BrNUFKeE54YnZadk1iNitzRWNIMFVVWUw5ZWZYQ0p2NVltSXV3NEpXUHhPamlYTSIsIm1hYyI6ImFlNmUyZGZkYTFjZjEyZDMwYTUxNGYwMmUyMzE0ZmIxMDRhMmQyMDdiZjNmZGRmOWVkNDcyOTExOWMzNTQ1OTIifQ%3D%3D',
    'hanime1_session': 'eyJpdiI6IjJYZFQ3REw1V3ZcL3VsWk10bGl1cnBRPT0iLCJ2YWx1ZSI6InRPT0FzTmx0S2dZZFU5dFdZdnI4T29zb2FCWEdKSGtlQ0Z4ZFZGTTlpWEVseUV6RXlyRDZYRThEV1BiVnRITHUiLCJtYWMiOiI5OTA5OWI3NzcyZWY1NWQxYTdkNGZjMzQ0OWUwNjFmZGJmNWVkMDM3ODVkNmQ5ODdhZWNiYTYxZTExNDUyYzNjIn0%3D',
    '__cf_bm': 'cGodoJYSOBFP5mep7CC7FlidHbJ_.3zncmvErCIzFHg-1675332040-0-AcKYXMxmBairSHhduMxtb+w3I9ic7WA1TwgbbFt47uvN78B/bFFeqWrYqwdgU643T2wzdUK+VLcFlafp6h7HpDFfbQ114CJUzpIfDdcCCxulfnxA93VPGqYjSAe+fQ/uBAHbstltdZbj3B12HZwHaoE=',
}

headers = {
    'authority': 'hanime1.me',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'max-age=0',
    # 'cookie': '__gads=ID=7f96118d9d1306a1-22d557512ed900bb:T=1673107879:RT=1673107879:S=ALNI_MbTqF10HkGZkXWkMmFxCE2tf6EErQ; _ga=GA1.2.1731675392.1673107870; __gpi=UID=00000b9f4fd7f0ca:T=1673107879:RT=1675168820:S=ALNI_MatOysPCRiuGJHlY9zCxCq7Y4uSBA; cf_clearance=CZy2TgB6bNhmG7ohtSqR9ptLlH4y2QVpVISIDgWbxas-1675175850-0-150; __atuvc=9%7C5; XSRF-TOKEN=eyJpdiI6ImRZRkVcL2JWWVwvOHBqQjNzeGEweFJjdz09IiwidmFsdWUiOiJBZHQ3TXN1TmtcL21JRjdMM1BrNUFKeE54YnZadk1iNitzRWNIMFVVWUw5ZWZYQ0p2NVltSXV3NEpXUHhPamlYTSIsIm1hYyI6ImFlNmUyZGZkYTFjZjEyZDMwYTUxNGYwMmUyMzE0ZmIxMDRhMmQyMDdiZjNmZGRmOWVkNDcyOTExOWMzNTQ1OTIifQ%3D%3D; hanime1_session=eyJpdiI6IjJYZFQ3REw1V3ZcL3VsWk10bGl1cnBRPT0iLCJ2YWx1ZSI6InRPT0FzTmx0S2dZZFU5dFdZdnI4T29zb2FCWEdKSGtlQ0Z4ZFZGTTlpWEVseUV6RXlyRDZYRThEV1BiVnRITHUiLCJtYWMiOiI5OTA5OWI3NzcyZWY1NWQxYTdkNGZjMzQ0OWUwNjFmZGJmNWVkMDM3ODVkNmQ5ODdhZWNiYTYxZTExNDUyYzNjIn0%3D; __cf_bm=cGodoJYSOBFP5mep7CC7FlidHbJ_.3zncmvErCIzFHg-1675332040-0-AcKYXMxmBairSHhduMxtb+w3I9ic7WA1TwgbbFt47uvN78B/bFFeqWrYqwdgU643T2wzdUK+VLcFlafp6h7HpDFfbQ114CJUzpIfDdcCCxulfnxA93VPGqYjSAe+fQ/uBAHbstltdZbj3B12HZwHaoE=',
    'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
}


proxies = requests_proxy

# -*- coding:utf-8 -*-
import requests
import time


cookie = ""

bh3payload = {"gids": "1"} #崩坏3
yspayload = {"gids": "2"} #原神
bh2payload = {"gids": "3"} #崩坏2
wdpayload = {"gids": "4"} #未定事件簿2
dbypayload = {"gids": "5"} #大别墅


while 1:
    url = "https://api-takumi.mihoyo.com/apihub/api/signIn"
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36 Edg/77.0.235.27',
        'Referer': 'https://bbs.mihoyo.com',
        'Sec-Fetch-Mode': 'cors',
        'Cookie': cookie,
        'Content-Type': 'application/json;charset=UTF-8'
    }

    bh3 = requests.post(url, headers=headers, json=bh3payload)
    ys = requests.post(url, headers=headers, json=yspayload)
    bh2 = requests.post(url, headers=headers, json=bh2payload)
    wd = requests.post(url, headers=headers, json=wdpayload)
    dby = requests.post(url, headers=headers, json=dbypayload)

    print("Start... \n", bh3.text, "米游社-崩坏3\n", ys.text, "米游社-原神\n", bh2.text, "米游社-崩坏2\n", wd.text, "米游社-未定事件簿\n",
          dby.text, "米游社-大别墅")
    print("休眠六小时...")

    time.sleep(21600)



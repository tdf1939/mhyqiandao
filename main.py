# -*- coding:utf-8 -*-
import requests
import json
import time


#填写cookie,自己登陆https://bbs.mihoyo.com/bh3/  F12进行抓取
cookie = ""

#休眠时间 单位/秒
setime = 21600

#参数，不要修改
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

    times = time.strftime('%Y.%m.%d %H:%M:%S ', time.localtime(time.time()))

    print(times, "开始执行游戏社区签到,Start")
    bh3 = requests.post(url, headers=headers, json=bh3payload)
    print(times, "崩坏3-米游社回显:", bh3.json()["message"])
    ys = requests.post(url, headers=headers, json=yspayload)
    print(times, "原神-米游社回显:", ys.json()["message"])
    bh2 = requests.post(url, headers=headers, json=bh2payload)
    print(times, "崩坏2-米游社回显:", bh2.json()["message"])
    wd = requests.post(url, headers=headers, json=wdpayload)
    print(times, "未定事件簿-米游社回显:", wd.json()["message"])
    dby = requests.post(url, headers=headers, json=dbypayload)
    print(times, "大别墅-米游社回显:", dby.json()["message"])

    print(times, "任务执行完成,休眠", setime, "秒...")

    time.sleep(setime)

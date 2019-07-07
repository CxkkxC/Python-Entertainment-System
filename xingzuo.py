# -*- coding: utf-8 -*-
import json, urllib
import requests
import xlrd
# 聚合接口星座运势
def request(xingzuo="", m="GET"):
    appkey = "5e1dde3cddaffdce0b47f2a5ac390135"
    url = "http://web.juhe.cn:8080/constellation/getAll"
    params = {
                "consName": xingzuo,#星座名称，如:双鱼座
                "type":"today", #运势类型：today,tomorrow,week,month,year
                "key": appkey
    }
    try:
        params = urllib.parse.urlencode(params)
        if m == "GET":
                    f = requests.get("%s?%s" % (url, params)).content.decode('utf-8')
        else:
                    f = requests.get(url, params).content.decode('utf-8')
        res = json.loads(f)
        if res:
            error_code = res["error_code"]
            if error_code == 0:
                return res
            else:
                return res["reason"]
        else:
            print("request api error")
    except:
        pass
    
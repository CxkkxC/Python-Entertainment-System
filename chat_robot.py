# -*- coding:utf-8 -*-
import urllib,json
from urllib import request
from urllib import parse
def getHtml(url, data):  
    page = request.urlopen(url,data)  
    html = page.read()
    html = html.decode("utf-8")  #decode()命令将网页的信息进行解码否则乱码
    return html  
def chat_robot(req_info):
    key= 'f461f3c34bc0401fbcfddded709b8b24'
    url = 'http://www.tuling123.com/openapi/api'
    #发给服务器数据
    query = {'key': key, 'info': req_info}
    data = parse.urlencode(query).encode('utf-8') 	#使用urlencode方法转换标准格式
            
    response = getHtml(url, data)  
    data = json.loads(response)  #字典数据
    return data['text']
    #print ('机器人: '+data['text'] )
    #print(chat_robot('退出'))
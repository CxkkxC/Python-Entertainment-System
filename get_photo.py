# -*- coding:utf-8 -*-
import requests,os #首先导入库
import  re
#设置默认配置
MaxSearchPage = 20 # 收索页数
CurrentPage = 0 # 当前正在搜索的页数
NeedSave = 0 # 是否需要储存
folder_path = ''#文件保存位置
#图片链接正则和下一页的链接正则
def imageFiler(content): # 通过正则获取当前页面的图片地址数组
          return re.findall('"objURL":"(.*?)"',content,re.S)
def nextSource(content): # 通过正则获取下一页的网址
          next = re.findall('<div id="page">.*<a href="(.*?)" class="n">',content,re.S)[0] 
          return next
#爬虫主体
def spidler(source):
          content = requests.get(source).text  # 通过链接获取内容
          imageArr = imageFiler(content) # 获取图片数组
          global CurrentPage
          for imageUrl in imageArr:
              global  NeedSave
              if NeedSave:  			# 如果需要保存图片则下载图片，否则不下载图片
                 global DefaultPath
                 try:
                      # 下载图片并设置超时时间,如果图片地址错误就不继续等待了
                      picture = requests.get(imageUrl,timeout=10) 
                 except:                   
                      continue
                 # 创建图片保存的路径
                 imageUrl = imageUrl.replace('/','').replace(':','').replace('?','')
                 pictureSavePath = imageUrl
                 fp = open(os.path.join(folder_path,pictureSavePath),'wb') # 以写入二进制的方式打开文件
                 fp.write(picture.content)
                 fp.close()
          global MaxSearchPage
          if CurrentPage <= MaxSearchPage:    #继续下一页爬取
               if nextSource(content):
                   CurrentPage += 1 
                   # 爬取完毕后通过下一页地址继续爬取
                   spidler("http://image.baidu.com" + nextSource(content)) 
#爬虫的开启方法
def  beginSearch(key,page=1):#page搜索页面，数字上加两页就是实际搜索页面，列如page=-1，实际搜索页面为一页 
          global MaxSearchPage,NeedSave,folder_path
          MaxSearchPage = page
          NeedSave = 1					#是否保存，值0不保存，1保存
          folder_path=key+"/"
          if os.path.exists(folder_path) == False:
            os.makedirs(folder_path)
          StartSource = "http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=" + str(key) + "&ct=201326592&v=flip" # 分析链接可以得到,替换其`word`值后面的数据来搜索关键词
          spidler(StartSource)
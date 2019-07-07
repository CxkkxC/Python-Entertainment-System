# -*- coding:utf-8 -*-
from tkinter import * 
from Adminview import * #菜单栏对应的各个子页面 
 
class AdminPage(object): 
 def __init__(self, master=None): 
  self.root = master #定义内部变量root 
  self.root.geometry('%dx%d' % (650, 400)) #设置窗口大小 
  self.createPage() 
 
 def createPage(self): 
  self.modifyPage = ModifyFrame(self.root) # 创建不同Frame 
  self.queryPage = QueryFrame(self.root) 
  self.countPage = CountFrame(self.root) 
  self.aboutPage = AboutFrame(self.root) 
  self.modifyPage.pack() #默认显示界面 
  menubar = Menu(self.root) 
  menubar.add_command(label='用户数据操作', command = self.modifyData) 
  menubar.add_command(label='用户资料查询', command = self.queryData) 
  menubar.add_command(label='用户信息统计', command = self.countData) 
  menubar.add_command(label='软件关于', command = self.aboutDisp) 
  self.root['menu'] = menubar # 设置菜单栏 
 
 def modifyData(self): 
  self.modifyPage.pack() 
  self.queryPage.pack_forget() 
  self.countPage.pack_forget() 
  self.aboutPage.pack_forget() 
 
 def queryData(self): 
  self.modifyPage.pack_forget() 
  self.queryPage.pack() 
  self.countPage.pack_forget() 
  self.aboutPage.pack_forget() 
 
 def countData(self): 
  self.modifyPage.pack_forget() 
  self.queryPage.pack_forget() 
  self.countPage.pack() 
  self.aboutPage.pack_forget() 
 
 def aboutDisp(self): 
  self.modifyPage.pack_forget() 
  self.queryPage.pack_forget() 
  self.countPage.pack_forget() 
  self.aboutPage.pack() 

# -*- coding:utf-8 -*-
from tkinter import * 
from Userview import * #菜单栏对应的各个子页面
from tkinter import *
from tkinter.messagebox import *
import  copy

 
class UserPage(object): 
 def __init__(self, master=None): 
  self.root = master #定义内部变量root 
  self.root.geometry('%dx%d' % (650, 400)) #设置窗口大小 
  self.createPage() 
 
 def createPage(self): 
  self.chatPage = ChatFrame(self.root) # 创建不同Frame 
  self.alterPage = alterFrame(self.root)
  self.gamePage = gameFrame(self.root)
  self.aboutPage = aboutFrame(self.root)
  self.chatPage.pack() #默认显示界面 
  menubar = Menu(self.root) 
  menubar.add_command(label='小艾机器人聊天页面', command = self.chatData)
  menubar.add_command(label='娱乐页面', command = self.gameData)
  menubar.add_command(label='用户资料修改', command = self.alterData)
  menubar.add_command(label='软件使用帮助', command = self.aboutData)
  self.root['menu'] = menubar # 设置菜单栏 
 
 def chatData(self): 
  self.chatPage.pack()
  self.gamePage.pack_forget()
  self.alterPage.pack_forget()
  self.aboutPage.pack_forget()
  
    
 def gameData(self): 
  self.chatPage.pack_forget()
  self.gamePage.pack()
  self.alterPage.pack_forget()
  self.aboutPage.pack_forget()
    

 def alterData(self): 
  self.chatPage.pack_forget()
  self.gamePage.pack_forget()
  self.alterPage.pack()
  self.aboutPage.pack_forget()
 
 def aboutData(self): 
  self.chatPage.pack_forget()
  self.gamePage.pack_forget()
  self.alterPage.pack_forget()
  self.aboutPage.pack()
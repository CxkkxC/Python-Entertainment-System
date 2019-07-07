# -*- coding:utf-8 -*-
from tkinter import * 
from tkinter.messagebox import * 
from linksql import * 
from get_photo import *
from tkinter import ttk 
from chat_robot import *
import  copy
import winsound
import re
from xingzuo import *


class ChatFrame(Frame): # 继承Frame类 
 def __init__(self, master=None):
  Frame.__init__(self, master) 
  self.root = master #定义内部变量root
  self.entry1=StringVar()
  self.createPage() 
 
 def createPage(self):
    def clear():
        for widget in self.winfo_children():
            widget.pack_forget()
        self.createPage()
    #def clear_entry_value():
        #self.entry1.delete(0,END)
        #self.entry1.focus_set()
    
    def send_message(event):
        try:
            str1=self.entry1.get()
            if str1 != "":
                strr =chat_robot(str1)
                Label(self,text="我："+str1).pack()
                Label(self, text="小艾机器人："+strr).pack()
            else:
                Label(self, text="退出聊天模式").pack()
        except:
            Label(self, text="联网发生异常，请联网重试！").pack()
    Entry(self,textvariable=self.entry1).pack()
    #self.btn1 = Button(text='重置', command=clear_entry_value)
    #self.btn1.pack()
    #button1=Button(self,text='发送', command=send_message).pack()
    self.root.bind('<KeyPress-Return>',send_message)#绑定键盘上的回车发送信息
    Button(self,text="清空聊天信息",command=clear).pack()
class gameFrame(Frame): # 继承Frame类 
 def __init__(self, master=None): 
  Frame.__init__(self, master) 
  self.root = master #定义内部变量root 
  self.createPage() 
 
 def createPage(self):
  def Getphoto():
    try:
        KeyWord=self.key_word.get()
        beginSearch(KeyWord,page=-1)
        showinfo(title='提示',message="下载已经完成，请打开文件夹<"+KeyWord+">查看!")
    except:
        showinfo(title='错误',message='请确认当前是否已经联网！')
    
  def number_music():
    try:
        MusicWord=self.music_word.get()
        if MusicWord=="":
            str1="11556654433221554433211556654433221"#如果输入为空默认为小星星简谱
        else:
            str1=MusicWord
        tone={'1':532,'2':588,'3':660,'4':698,'5':784,'6':880,'7':988}
        a=list(str1)
        b=len(a)
        for i in range(b):
            winsound.Beep(tone[a[i]],400)
    except:
        showinfo(title='错误',message='出错啦！请输入1-7的数字')
  def MAin():
        roo=Toplevel(self.root)
        roo.title("推箱子")
        imgs= [PhotoImage(file='bmp\\Wall.gif'),
               PhotoImage(file='bmp\\Worker.gif'),
               PhotoImage(file='bmp\\Box.gif'),
               PhotoImage(file='bmp\\Passageway.gif'),
               PhotoImage(file='bmp\\Destination.gif'),
               PhotoImage(file='bmp\\WorkerInDest.gif'),
               PhotoImage(file='bmp\\RedBox.gif') ]
        #0代表墙，1代表人，2代表箱子，3代表路，4代表目的地
        #5代表人在目的地，6代表放到目的地的箱子
        Wall = 0
        Worker = 1 
        Box = 2
        Passageway = 3
        Destination = 4
        WorkerInDest = 5
        RedBox = 6
        #原始地图
        myArray1 = [[0,3,1,4,3,3,3],
                   [0,3,3,2,3,3,0],  
                   [0,0,3,0,3,3,0],
                   [3,3,2,3,0,0,0],
                   [3,4,3,3,3,0,0],
                   [0,0,3,3,3,3,0],
                   [0,0,0,0,0,0,0]]
        #绘制整个游戏区域图形
        def drawGameImage( ):
            global x,y

            for i in range(0,7) :#0--6
               for j in range(0,7) :#0--6
                    if myArray[i][j] == Worker :
                       x=i  #工人当前位置(x,y)
                       y=j
                       #print("工人当前位置:",x,y)
                    img1= imgs[myArray[i][j]]
                    cv.create_image((i*32+20,j*32+20),image=img1)
                    cv.pack()
            #print (myArray)

        def callback(event) :#按键处理
            global x,y,myArray
            #print ("按下键：", event.char)
            KeyCode = event.keysym
            #工人当前位置(x,y)	        
            if KeyCode=="Up":#分析按键消息
            #向上
                    x1 = x;
                    y1 = y - 1;
                    x2 = x;
                    y2 = y - 2;
                    #将所有位置输入以判断并作地图更新
                    MoveTo(x1, y1, x2, y2);
            #向下
            elif KeyCode=="Down":
                    x1 = x;
                    y1 = y + 1;
                    x2 = x;
                    y2 = y + 2;
                    MoveTo(x1, y1, x2, y2);
            #向左
            elif KeyCode=="Left":
                    x1 = x - 1;
                    y1 = y;
                    x2 = x - 2;
                    y2 = y;
                    MoveTo(x1, y1, x2, y2);
            #向右
            elif KeyCode=="Right":
                    x1 = x + 1;
                    y1 = y;
                    x2 = x + 2;
                    y2 = y;
                    MoveTo(x1, y1, x2, y2);
            elif KeyCode=="space": #空格键
               #print ("按下键：空格", event.char)
               myArray=copy.deepcopy(myArray1)  #恢复原始地图
               drawGameImage( )

        #判断是否在游戏区域
        def IsInGameArea(row, col) :
            return (row >= 0 and row < 7 and col >= 0 and col < 7) 
        def MoveTo(x1, y1, x2, y2) :
                global x,y
                P1=None
                P2=None
                if IsInGameArea(x1, y1) : #判断是否在游戏区域
                    P1=myArray[x1][y1];
                if IsInGameArea(x2, y2) :
                    P2 = myArray[x2][y2]
                if P1 ==  Passageway :#P1处为通道
                    MoveMan(x,y);
                    x = x1; y = y1;
                    myArray[x1][y1] =  Worker; 
                if P1 ==  Destination :#P1处为目的地
                    MoveMan(x, y);
                    x = x1; y = y1;
                    myArray[x1][y1] =  WorkerInDest;
                if P1 ==  Wall or  not IsInGameArea(x1, y1) :
                    #P1处为墙或出界
                    return;

                #以下P1处为箱子
                if P1 ==  Box  :#P1处为箱子
                   if P2 ==  Wall or  not IsInGameArea(x1, y1) or P2 ==  Box :##P2处为墙或出界
                      return;


                #P1处为箱子,P2处为通道
                if P1 ==  Box and P2 ==  Passageway :
                    MoveMan(x, y);
                    x = x1; y = y1;
                    myArray[x2][y2]= Box;
                    myArray[x1][y1] =  Worker;
                if P1 ==  Box and P2 ==  Destination :
                    MoveMan(x, y);
                    x = x1; y = y1;
                    myArray[x2][y2]= RedBox;
                    myArray[x1][y1] =  Worker;
                #P1处为放到目的地的箱子,P2处为通道
                if P1 ==  RedBox and P2 ==  Passageway :
                    MoveMan(x, y);
                    x = x1; y = y1;
                    myArray[x2][y2] =  Box;
                    myArray[x1][y1] =  WorkerInDest;
                #P1处为放到目的地的箱子,P2处为目的地
                if P1 ==  RedBox and P2 ==  Destination :
                    MoveMan(x, y);
                    x = x1; y = y1;
                    myArray[x2][y2] =  RedBox;
                    myArray[x1][y1] =  WorkerInDest;
                drawGameImage()
                #这里要验证是否过关
                if IsFinish() :
                    showinfo(title="提示",message=" 恭喜你顺利过关" ) 
                    
                 

        def  MoveMan(x, y) :
            if myArray[x][y] == Worker :
                myArray[x][y] = Passageway;
            elif myArray[x][y] == WorkerInDest :
                myArray[x][y] = Destination;


        def IsFinish( ):#验证是否过关
            bFinish = True;
            for i in range(0,7) :#0--6
               for j in range(0,7) :#0--6
                    if  (myArray[i][j] == Destination
                           or myArray[i][j] == WorkerInDest) :
                        bFinish = False;
            return bFinish;



        def drawQiPan( ) :#画棋盘
            for i in range(0,15) :
                cv.create_line(20,20+40*i,580,20+40*i,width=2)
            for i in range(0,15) :
                cv.create_line(20+40*i,20,20+40*i,580,width=2)
            cv.pack()


        def print_map( ) :#输出map地图
            for i in range(0,15) :#0--14 
               for j in range(0,15) :#0--14
                   print (map[i][j],end=' ')
               print ('w')

        cv = Canvas(roo, bg = 'green', width = 226, height = 226)
        #drawQiPan( )
        myArray=copy.deepcopy(myArray1) 
        drawGameImage()    
        cv.bind("<KeyPress>", callback)
        cv.pack()
        cv.focus_set() #将焦点设置到cv上
  def print_jp():
    def Cxk(event):
        try:
            tone={'1':530,'2':588,'3':660,'4':698,'5':784,'6':880,'7':988}
            a=str(event.char)
            b=a.strip()
            winsound.Beep(tone[b],400)
        except:
            pass
    windows = Toplevel(self.root)
    windows.title("我的窗口")
    windows.geometry("150x150")
    Label(windows, text='输入一个数字发出一个声音\r\n（仅限数字键盘上的1-7）').pack()
    Entry(windows,fg='red').pack()
    windows.bind('<KeyPress>',Cxk)
  self.key_word=StringVar()
  self.music_word=StringVar()
  Label(self,fg='blue', text='图片下载期间软件稍有卡顿，请您耐心等候！').pack()
  Label(self, text='请输入关键词：').pack()
  Entry(self,textvariable=self.key_word).pack()
  Button(self,text="查找并下载图片",command=Getphoto).pack()
  Button(self,text="推箱子游戏",command=MAin).pack()
  Label(self,text='请输入数字简谱：').pack()
  Entry(self,textvariable=self.music_word).pack()
  Button(self,text="数字钢琴曲",command=number_music).pack()
  Button(self,text="数字钢琴曲自创",command=print_jp).pack()
  

class alterFrame(Frame): # 继承Frame类 
 def __init__(self, master=None): 
  Frame.__init__(self, master) 
  self.root = master #定义内部变量root
  self.createPage() 
 
 def createPage(self):
  def get_xingzuo():
    try:
        xingzuo = self.xingzuo.get()
        a=request(xingzuo,"GET")
        xingzuo_info="%s星座%s运势\r\n幸运色：%s\r\n健康状态：%s\r\n爱情指数：%s\r\n金钱指数：%s\r\n幸运数字：%d\r\n幸运星座：%s\r\n运势：%s\r\n工作状态：%s" % (a["name"],a["datetime"],a["color"],a["health"],a["love"],a["money"],a["number"],a["QFriend"],a["summary"],a["work"])
        showinfo(title='Cxk',message=xingzuo_info)
    except:
        showinfo(title='错误',message='请确认星座是否输入正确！')
  def alter_user_sql():
    def alter_sql():
        try:
            alter_age = self.alter_age.get()
            alter_id = self.alter_id.get()
            alter_name = self.alter_name.get()
            alter_pw = self.alter_pw.get()
            old_id=self.user_alter_id1.get()
            cxk2=user_showdb(old_id)
            if cxk2 != None:
                user_alter(old_id,alter_id,alter_name,alter_pw,alter_age)
                showinfo(title='提示', message='用户资料修改成功')
                root1.destroy()
            else:
                showinfo(title='提示',message='用户账号获取失败')
        except:
            showinfo(title='错误',message='请确认当前账号是否输入正确！')
    root1=Toplevel(self.root)
    root1.title("修改资料窗口")
    root1.geometry('300x250')
    
    self.user_alter_id1=StringVar()
    Label(root1, text='请输入当前账号：').pack()
    Entry(root1,textvariable=self.user_alter_id1).pack()
    
    self.alter_name = StringVar()
    Label(root1, text='新的姓名: ').pack()
    Entry(root1, textvariable=self.alter_name).pack()

    self.alter_age= StringVar()
    Label(root1, text='新的年龄: ').pack()
    Entry(root1, textvariable=self.alter_age).pack()

    self.alter_id = StringVar()
    Label(root1, text='新的账号: ').pack()
    Entry(root1, textvariable=self.alter_id).pack()

    self.alter_pw = StringVar()
    Label(root1, text='新的密码: ').pack()
    Entry(root1, textvariable=self.alter_pw).pack()
    Button(root1, text='确认修改', command=alter_sql).pack()
    
  self.xingzuo=StringVar()
  Label(self, text='请输入您的星座：').pack()
  Entry(self,textvariable=self.xingzuo).pack()
  Button(self,text="查看星座今日运势",command=get_xingzuo).pack()
        
  Button(self,text="修改个人资料",command=alter_user_sql).pack()

class aboutFrame(Frame): # 继承Frame类 
 def __init__(self, master=None): 
  Frame.__init__(self, master) 
  self.root = master #定义内部变量root 
  self.createPage() 
 
 def createPage(self): 
  Label(self, fg='blue',text='软件关于界面\r\n1:小艾聊天机器人简介:智能工具:生活百科,图片搜索,数字计算,问答百科\r\n语料库:中英互译,聊天对话,休闲娱乐,笑话大全,故事大全\r\n成语接龙,新闻资讯,星座运势,脑筋急转弯,歇后语,绕口令,顺口溜,天气查询,每天可调用次数为一百次\r\n2:关键字下载图片，同一关键字下载图片都是一样的，\r\n可以变换关键字下载，图片存在当前目录下，文件夹名为关键字名。\r\n推箱子，只有一关。。\r\n钢琴简谱音乐：输入1-7的数字字符串转换播放为声音：都累吗发售拉稀。\r\n不输入默认播放小星星简谱：11556654433221554433211556654433221\r\n3:个人资料修改').pack() 


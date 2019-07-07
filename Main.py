# -*- coding:utf-8 -*-
from tkinter.messagebox import * 
from tkinter import *
from AdminPage import *
from linksql import * 
from UserPage import *
import time

class LoginPage(object):
    
    def __init__(self, master=None):
        
        self.root = master
        self.root.geometry("650x400") 
        self.user_id = StringVar()
        self.user_pw = StringVar() 
        self.createPage()
        
    def createPage(self):
        '''
        登录页面
        1:创建图片组件
        2:根目录基础上添加Frame容器
        3:Frame容器上添加注册控件
        '''
        bm=PhotoImage(file=r'cxk.gif')
        self.lab3=Label(self.root,image=bm)
        self.lab3.bm=bm
        self.lab3.pack()
        
        self.page = Frame(self.root) 
        self.page.pack()
        Label(self.page).grid(row=0, stick=W) 
        Label(self.page, text = '账户: ').grid(row=1, stick=W, pady=10) 
        Entry(self.page, textvariable=self.user_id).grid(row=1, column=1, stick=E) 
        Label(self.page, text = '密码: ').grid(row=2, stick=W, pady=10) 
        Entry(self.page, textvariable=self.user_pw, show='*').grid(row=2, column=1, stick=E) 
        Button(self.page, text='管理登录', command=self.admin_loginCheck).grid(row=3, column=0)
        #self.root.bind('<KeyPress-Return>',self.admin_loginCheck1)#绑定键盘上的回车登录
        Button(self.page, text='用户注册',command=self.signup).grid(row=3, column=3) 
        Button(self.page, text='用户登录', command=self.user_loginCheck).grid(row=3,column=1) 
        #self.root.bind('<KeyPress-Return>',self.user_loginCheck1)#绑定键盘上的回车登录
    '''
    #账号密码正确时，回车登录自动识别是管理员还是用户
    #回车登录或者按钮登录时要设置两个登录函数按钮登录传入一个参数self，回车登录传入两个参数self，键盘事件event
    #有bug，窗口中变量没有释放，在使用聊天界面时按回车时会跳出登录提示。。。。
    def admin_loginCheck1(self,event):
            Admin_id=self.user_id.get()
            #print(Admin_id)
            Admin_pw=self.user_pw.get()
            #print(Admin_pw)
            pd=admin_Select_id_pw(Admin_id,Admin_pw)
            if pd:
                self.page.destroy()
                self.lab3.pack_forget()
                AdminPage(self.root)
            else:
                showinfo(title='错误', message='账号或密码错误！')
    
    def user_loginCheck1(self,event):
        User_id=self.user_id.get()
        #print(User_id)
        User_pw=self.user_pw.get()
        #print(User_pw)
        pd=user_Select_id_pw(User_id,User_pw)
        if pd:
            self.page.destroy()
            self.lab3.pack_forget()
            UserPage(self.root)
        else:
            showinfo(title='错误', message='账号或密码错误！')
    '''
        
    def admin_loginCheck(self):
        '''
        管理员登录
        1:获取管理员账号与密码
        2:将获取到的账号与密码与数据库文件配对，配对成功返回值为正确，否则为错误
        3:将返回值判断，正确则登录界面清除，登录界面图片清除，进入管理员界面
        异常捕获：未填写账号或者密码
        '''
        try:
            Admin_id=self.user_id.get()
            #print(Admin_id)
            Admin_pw=self.user_pw.get()
            #print(Admin_pw)
            pd=admin_Select_id_pw(Admin_id,Admin_pw)
            if pd:
                self.page.destroy()
                self.lab3.pack_forget()
                AdminPage(self.root)
            else:
                showinfo(title='错误', message='账号或密码错误！')
        except:
                showinfo(title='错误',message='输入错误，请重新输入！')

    def user_loginCheck(self):
        '''
        用户登录
        1:获取用户账号与密码
        2:将获取到的账号与密码与数据库文件配对，配对成功返回值为正确，否则为错误
        3:将返回值判断，正确则登录界面清除，登录界面图片清除，进入用户界面，异常捕获：未填写账号或者密码
        '''
        try:
            User_id=self.user_id.get()
            #print(User_id)
            User_pw=self.user_pw.get()
            #print(User_pw)
            pd=user_Select_id_pw(User_id,User_pw)
            if pd:
                self.page.destroy()
                self.lab3.pack_forget()
                UserPage(self.root)
            else:
                showinfo(title='错误', message='账号或密码错误！')
        except:
            showinfo(title='错误',message='输入错误，请重新输入！')
                
    
    def signup(self):
        '''
        用户注册页面
        1:新建一个置于顶层的窗口
        2:将布局控件放入
        3:每个窗口的控件布局必须是一致的，place(),grid(),pack()中的一种
        '''
        def insert_sql():
            '''
            添加用户
            1:获取用户姓名，年龄，账号，密码
            2:将获取到的账号与数据库文件配对，查看是否存在相同账号，如不存在，将用户插入数据库文件，存在则提示修改账户名
            异常捕获：信息未填写
            '''
            try:
                age = self.new_age.get()
                id = self.new_id.get()
                name = self.new_name.get()
                pw = self.new_pw.get()
                cxk=user_showdb(id)
                if cxk == None:
                    user_InsertData(id,name,pw,age)
                    showinfo(title='提示', message='用户注册成功')
                    self.window_sign_up.destroy()
                else:
                    showinfo(title='提示',message='账户重复，注册失败，请修改账户名！')  
            except:
                showinfo(title='错误',message='输入错误，请重新输入！')
                

        self.window_sign_up = Toplevel(self.root)
        self.window_sign_up.geometry('300x200')
        self.window_sign_up.title('注册窗口')

        self.new_name = StringVar()
        Label(self.window_sign_up, text='姓名: ').place(x=10, y=10) 
        entry_new_name = Entry(self.window_sign_up, textvariable=self.new_name) 
        entry_new_name.place(x=130, y=10)

        self.new_age= StringVar()
        Label(self.window_sign_up, text='年龄: ').place(x=10, y=50)
        entry_usr_age = Entry(self.window_sign_up, textvariable=self.new_age)
        entry_usr_age.place(x=130, y=50)

        self.new_id = StringVar()
        Label(self.window_sign_up, text='账号: ').place(x=10, y=90)
        entry_usr_id = Entry(self.window_sign_up, textvariable=self.new_id)
        entry_usr_id.place(x=130, y=90)
        
        self.new_pw = StringVar()
        Label(self.window_sign_up, text='密码: ').place(x=10, y=130)
        entry_usr_pw = Entry(self.window_sign_up, textvariable=self.new_pw, show='*')
        entry_usr_pw.place(x=130, y=130)

        sign_up = Button(self.window_sign_up, text='注册', command=insert_sql)
        sign_up.place(x=237, y=160)
 
root = Tk() #建立一个根窗口，所有窗口的基础
root.title('Cxk娱乐系统')
LoginPage(root)#进入调用登录
#获取本地时间戳转换成字符串进行使用after()动态显示，after - 等待一段时间后再执行命令
Label1=Label(fg='blue',text="当前时间为："+time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
Label1.pack()
def trickit():
    currentTime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    Label1.config(text="当前时间为："+currentTime)
    root.update()
    Label1.after(1000, trickit)
Label1.after(1000, trickit)
root.mainloop()   
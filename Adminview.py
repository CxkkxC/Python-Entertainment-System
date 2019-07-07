# -*- coding:utf-8 -*-
from tkinter import * 
from tkinter.messagebox import * 
from linksql import * 
from tkinter import ttk 
 
class ModifyFrame(Frame): # 继承Frame类 
 def __init__(self, master=None):
  Frame.__init__(self, master) 
  self.root = master #定义内部变量root  
  self.createPage() 
        
 def createPage(self):
    def insert_user_sql():
        try:
            age = self.new_age.get()
            id = self.new_id.get()
            name = self.new_name.get()
            pw = self.new_pw.get()
            cxk=user_showdb(id)
            if cxk == None:
                user_InsertData(id,name,pw,age)
                showinfo(title='提示', message='用户注册成功')
            else:
                showinfo(title='提示',message='账户重复，注册失败，请修改账户名！') 
        except:
            showinfo(title='错误',message='输入错误，请重新输入！')
    def insert_admin_sql():
        try:
            age = self.new_age.get()
            id = self.new_id.get()
            name = self.new_name.get()
            pw = self.new_pw.get()
            cxk=admin_showdb(id)
            if cxk == None:
                admin_InsertData(id,name,pw,age)
                showinfo(title='提示', message='管理员添加成功')
            else:
                showinfo(title='提示',message='账户重复，注册失败，请修改账户名！') 
        except:
            showinfo(title='错误',message='输入错误，请重新输入！')
    def del_user_sql():
        try:
            del_id=self.del_id.get()
            cxk1=user_showdb(del_id)
            if cxk1==None:
                showinfo(title='提示',message='账户删除失败，无该账户，请重新检查账户名是否正确再进行删除！') 
            else:
                user_deldb(del_id)
                cxk2=user_showdb(del_id)
                if cxk2 == None:
                    Label(self, text="你已经成功删除以下用户：").pack()
                    Label(self, text=cxk1).pack()
                else:
                    showinfo(title='提示',message='账户删除失败，请重新检查账户名是否正确再进行删除！') 
        except:
            showinfo(title='错误',message='用户账号输入错误，请重新输入！')
    
    def del_admin_sql():
        try:
            del_id=self.del_id.get()
            cxk1=str(admin_showdb(del_id))
            if cxk1==None:
                showinfo(title='提示',message='账户删除失败，无该账户，请重新检查账户名是否正确再进行删除！')
            else:
                admin_deldb(del_id)
                cxk2=admin_showdb(del_id)
                if cxk2 == None:
                    #Label(self, text="你已经成功删除以下管理员：").pack()
                    showinfo(title='提示',message="你已成功删除该管理员："+cxk1)
                else:
                    showinfo(title='提示',message='账户删除失败，请重新检查账户名是否正确再进行删除！') 
        except:
            showinfo(title='错误',message='管理员账号输入错误，请重新输入！')
                
    self.new_name = StringVar()
    Label(self, text='姓名: ').pack()
    Entry(self, textvariable=self.new_name).pack()

    self.new_age= StringVar()
    Label(self, text='年龄: ').pack()
    Entry(self, textvariable=self.new_age).pack()

    self.new_id = StringVar()
    Label(self, text='账号: ').pack()
    Entry(self, textvariable=self.new_id).pack()

    self.new_pw = StringVar()
    Label(self, text='密码: ').pack()
    Entry(self, textvariable=self.new_pw, show='*').pack()
    Button(self,text='添加用户',command=insert_user_sql).pack()
    Button(self,text='添加管理员',command=insert_admin_sql).pack()
    
    self.del_id=StringVar()
    Label(self, text='请输入想要删除的用户/管理员账号: ').pack()
    Entry(self, textvariable=self.del_id).pack()
    Button(self,text='删除用户',command=del_user_sql).pack()
    Button(self,text='删除管理员',command=del_admin_sql).pack()
 
class QueryFrame(Frame): # 继承Frame类 
 def __init__(self, master=None): 
  Frame.__init__(self, master) 
  self.root = master #定义内部变量root
  self.get_info=StringVar()
  self.createPage() 
 
 def createPage(self):
    def clear():
        for widget in self.winfo_children():
            widget.pack_forget()
        self.createPage()
    def get_infor():
        try:
            s=self.get_info.get()
            str=user_showdb(s)
            if str==None:
                Label(self,text="无该用户账号，请重新输入！").pack()
            else:
                Label(self,text="用户账号为："+s+" 的信息如下：").pack()
                Label(self,text=str).pack()
        except:
            showinfo(title='错误',message='输入错误，请重新输入！')
    Button(self,text="清空查询信息",command=clear).pack()        
    Label(self,text="输入用户账号查询：").pack()
    Entry(self,textvariable=self.get_info).pack()
    Button(self,text="查询",command=get_infor).pack()
    Label(self,text="全部用户信息").pack()
    def dayin(chioce):
        s1=user_SelectTable()
        c=int(chioce)
        Label(self,text=s1[c],font = ('微软雅黑',13)).pack()
    def go(*args):#处理事件，*args表示可变参数
        dayin(comboxlist.get()) #打印选中的值
    comvalue=StringVar()#窗体自带的文本，新建一个值
    comboxlist=ttk.Combobox(self,textvariable=comvalue) #初始化
    a=user_SelectTable()
    a=len(a)
    a=a-1
    b=[]
    while a>=0:
        a=str(a)
        b.append(a)
        a=int(a)
        a-=1
    c=tuple(b)
    comboxlist["values"]=c
    comboxlist.current(0)  #选择第一个
    comboxlist.bind("<<ComboboxSelected>>",go) #绑定事件,(下拉列表框被选中时，绑定go()函数)
    comboxlist.pack()
    Label(self,text="账户      姓名     密码     年龄",fg='red',font = ('微软雅黑',10)).pack()
class CountFrame(Frame): # 继承Frame类 
 def __init__(self, master=None): 
  Frame.__init__(self, master) 
  self.root = master #定义内部变量root 
  self.createPage() 
 
 def createPage(self): 
  Label(self, text='统计界面').pack() 
 
 
class AboutFrame(Frame): # 继承Frame类 
 def __init__(self, master=None): 
  Frame.__init__(self, master) 
  self.root = master #定义内部变量root 
  self.createPage() 
 
 def createPage(self): 
  Label(self,fg='blue', text='关于管理员界面\r\n对软件使用用户进行增删改查，管理员添加管理员').pack() 

# -*- coding:utf-8 -*-
import sqlite3
# 打开用户数据库
def user_opendb():
        conn = sqlite3.connect("persons.db")
        cur = conn.execute("""create table if not exists renyuan(userid varchar(128),username varchar(128),
        passworld varchar(128),age integer)""")
        return cur, conn
#查询用户全部信息
def user_SelectTable():
        hel = user_opendb()
        cur = hel[1].cursor()
        cur.execute("select * from renyuan")
        res = cur.fetchall()
        #for line in res:
                #for h in line:
                        #print(h),
                #print(line)
        return res
        cur.close()
#  往用户数据库中添加内容
def user_InsertData(id,name,pw,age):
        id=str(id)
        pw=str(pw)
        hel = user_opendb()
        hel[1].execute("insert into renyuan(userid,username, passworld,age)values (?,?,?,?)",(id,name,pw,age))
        hel[1].commit()
        hel[1].close()
#查询用户个人信息
def user_showdb(userid):
        userid=str(userid)
        hel = user_opendb()
        cur = hel[1].cursor()
        cur.execute("select * from renyuan where userid="+userid)
        res = cur.fetchone()
        cur.close()
        return res
#   删除用户数据库中的全部内容
def user_delalldb():
        hel = user_opendb()              # 返回游标conn
        hel[1].execute("delete from renyuan")
        print("ok")
        hel[1].commit()
        hel[1].close()
#   删除用户数据库中的指定内容
def user_deldb(id):
        id=str(id)
        hel = user_opendb()              # 返回游标conn
        hel[1].execute("delete from renyuan where userid="+id)
        #print("ok")
        hel[1].commit()
        hel[1].close()
        
#  修改用户数据库的内容
def user_alter(id1,id2,name,pw,age):
        id1=str(id1)
        id2=str(id2)
        hel = user_opendb()
        hel[1].execute("update renyuan set userid=?,username=?, passworld= ?,age=? where userid="+id1,(id2,name,pw,age))
        hel[1].commit()
        hel[1].close()
# 查询用户数据
def user_Select_id_pw(id,pw):
        id=str(id)
        pw=str(pw)
        hel = user_opendb()
        cur = hel[1].cursor()
        cur.execute("select * from renyuan where userid="+id+" and passworld= "+pw)
        hel[1].commit()
        for row in cur:
            if row:
                return True
            else:
                return False
        cur.close()
        hel[1].close()
#---------------------------------------------------------------------------------------------------#

# 打开管理员数据库
def admin_opendb():
        conn = sqlite3.connect("persons.db")
        cur = conn.execute("""create table if not exists admin(userid varchar(128),username varchar(128),
        passworld varchar(128),age integer)""")
        return cur, conn
#查询管理员全部信息
def admin_SelectTable():
        hel = admin_opendb()
        cur = hel[1].cursor()
        cur.execute("select * from admin")
        res = cur.fetchall()
        #for line in res:
                #for h in line:
                        #print(h),
                #print(line)
        return res
        cur.close()
#  往管理员数据库中添加内容
def admin_InsertData(id,name,pw,age):
        id=str(id)
        pw=str(pw)
        hel = admin_opendb()
        hel[1].execute("insert into admin(userid,username, passworld,age)values (?,?,?,?)",(id,name,pw,age))
        hel[1].commit()
        hel[1].close()
#查询管理员个人信息
def admin_showdb(userid):
        userid=str(userid)
        hel = admin_opendb()
        cur = hel[1].cursor()
        cur.execute("select * from admin where userid="+userid)
        res = cur.fetchone()
        cur.close()
        return res
#   删除管理员数据库中的全部内容
def admin_delalldb():
        hel = admin_opendb()              # 返回游标conn
        hel[1].execute("delete from admin")
        print("ok")
        hel[1].commit()
        hel[1].close()
#   删除管理员数据库中的指定内容
def admin_deldb(id):
        id=str(id)
        hel = admin_opendb()              # 返回游标conn
        hel[1].execute("delete from admin where userid="+id)
        #print("ok")
        hel[1].commit()
        hel[1].close()
        
#  修改管理员数据库的内容
def admin_alter(id,id2,name,pw,age):
        id=str(id)
        id2=str(id2)
        hel = admin_opendb()
        hel[1].execute("update admin set usernid=?,username=?, passworld= ?,age=? where userid="+id,(id2,name,pw,age))
        hel[1].commit()
        hel[1].close()
# 查询管理员数据
def admin_Select_id_pw(id,pw):
        id=str(id)
        pw=str(pw)
        hel = admin_opendb()
        cur = hel[1].cursor()
        cur.execute("select * from admin where userid="+id+" and passworld= "+pw)
        hel[1].commit()
        for row in cur:
            if row:
                return True
            else:
                return False
        cur.close()
        hel[1].close()
